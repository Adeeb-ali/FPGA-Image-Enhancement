import os
import sys
import time
import pandas as pd
import torch
import numpy as np
import cv2

from torchvision.utils import save_image
from skimage.metrics import structural_similarity

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))

sys.path.append(CURRENT_DIR)
sys.path.append(ROOT_DIR)

from model_builder import build_model

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"\nUsing Device: {DEVICE}")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "best_model_arch1.pth"
)

CLEAN_DIR = os.path.join(
    BASE_DIR,
    "..",
    "testing_images",
    "clean"
)

DEG_DIR = os.path.join(
    BASE_DIR,
    "..",
    "testing_images",
    "degraded"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "..",
    "outputs"
)

IMG_DIR = os.path.join(OUTPUT_DIR, "enhanced")
COMPARE_DIR = os.path.join(OUTPUT_DIR, "comparison")
METRIC_DIR = os.path.join(OUTPUT_DIR, "metrics")

os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(COMPARE_DIR, exist_ok=True)
os.makedirs(METRIC_DIR, exist_ok=True)

NUM_IMAGES = 100
PSNR_SKIP_THRESHOLD = 40.0


def compute_psnr(a, b):

    mse = torch.mean((a - b) ** 2).item()

    if mse == 0:
        return 100.0

    return float(10 * np.log10(1.0 / mse))


def compute_ssim(a, b):

    a = a.squeeze().permute(1, 2, 0).cpu().numpy()
    b = b.squeeze().permute(1, 2, 0).cpu().numpy()

    return float(
        structural_similarity(
            a,
            b,
            channel_axis=2,
            data_range=1.0
        )
    )


print("\nLoading Model...")

ckpt = torch.load(
    MODEL_PATH,
    map_location=DEVICE
)

model = build_model(
    ckpt["config"]
).to(DEVICE)

model.load_state_dict(
    ckpt["model_state"]
)

model.eval()

print("Model Loaded")

files = sorted(
    list(
        set(os.listdir(CLEAN_DIR)) &
        set(os.listdir(DEG_DIR))
    )
)

print(f"\nMatched Images: {len(files)}")

rows = []

total_psnr_before = 0
total_psnr_after = 0

total_ssim_before = 0
total_ssim_after = 0

processed_images = 0
skipped_images = 0

start_total = time.time()

with torch.no_grad():

    for i, name in enumerate(files):

        if processed_images >= NUM_IMAGES:
            break

        print(f"\nProcessing: {name}")

        clean_path = os.path.join(CLEAN_DIR, name)
        deg_path = os.path.join(DEG_DIR, name)

        clean = cv2.imread(clean_path)
        deg = cv2.imread(deg_path)

        if clean is None or deg is None:
            print("Failed to read image")
            continue

        clean = cv2.cvtColor(
            clean,
            cv2.COLOR_BGR2RGB
        ) / 255.0

        deg = cv2.cvtColor(
            deg,
            cv2.COLOR_BGR2RGB
        ) / 255.0

        clean_tensor = torch.tensor(clean)\
            .permute(2, 0, 1)\
            .unsqueeze(0)\
            .float()\
            .to(DEVICE)

        deg_tensor = torch.tensor(deg)\
            .permute(2, 0, 1)\
            .unsqueeze(0)\
            .float()\
            .to(DEVICE)

        psnr_before = compute_psnr(
            deg_tensor,
            clean_tensor
        )

        if psnr_before > PSNR_SKIP_THRESHOLD:

            skipped_images += 1

            print(
                f"Skipped "
                f"(PSNR={psnr_before:.2f})"
            )

            continue

        start_inf = time.time()

        out = model(deg_tensor)

        inference_time = time.time() - start_inf

        out = torch.clamp(out, 0, 1)

        psnr_after = compute_psnr(
            out,
            clean_tensor
        )

        ssim_before = compute_ssim(
            deg_tensor,
            clean_tensor
        )

        ssim_after = compute_ssim(
            out,
            clean_tensor
        )

        gain = psnr_after - psnr_before

        print(
            f"PSNR : "
            f"{psnr_before:.2f} -> "
            f"{psnr_after:.2f}"
        )

        print(
            f"SSIM : "
            f"{ssim_before:.4f} -> "
            f"{ssim_after:.4f}"
        )

        print(
            f"Gain : {gain:.2f} dB"
        )

        print(
            f"Inference : "
            f"{inference_time:.4f} sec"
        )

        save_image(
            out,
            os.path.join(
                IMG_DIR,
                f"{processed_images}_enhanced.jpg"
            )
        )

        input_np = deg_tensor.squeeze()\
            .permute(1, 2, 0)\
            .cpu()\
            .numpy()

        output_np = out.squeeze()\
            .permute(1, 2, 0)\
            .cpu()\
            .numpy()

        gt_np = clean_tensor.squeeze()\
            .permute(1, 2, 0)\
            .cpu()\
            .numpy()

        input_img = (input_np * 255).astype(np.uint8)
        output_img = (output_np * 255).astype(np.uint8)
        gt_img = (gt_np * 255).astype(np.uint8)

        cv2.putText(
            input_img,
            "INPUT",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        cv2.putText(
            output_img,
            "OUTPUT",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            gt_img,
            "GROUND TRUTH",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        comparison = np.hstack([
            input_img,
            output_img,
            gt_img
        ])

        comparison = cv2.cvtColor(
            comparison,
            cv2.COLOR_RGB2BGR
        )

        compare_path = os.path.join(
            COMPARE_DIR,
            f"{processed_images}_compare.jpg"
        )

        cv2.imwrite(
            compare_path,
            comparison
        )

        rows.append({

            "image": name,

            "psnr_before": psnr_before,
            "psnr_after": psnr_after,

            "ssim_before": ssim_before,
            "ssim_after": ssim_after,

            "gain": gain,

            "inference_time_sec": inference_time
        })

        total_psnr_before += psnr_before
        total_psnr_after += psnr_after

        total_ssim_before += ssim_before
        total_ssim_after += ssim_after

        processed_images += 1

df = pd.DataFrame(rows)

df = df.sort_values(
    by="gain",
    ascending=False
)

csv_path = os.path.join(
    METRIC_DIR,
    "results.csv"
)

df.to_csv(
    csv_path,
    index=False
)

total_time = time.time() - start_total

if processed_images > 0:

    avg_psnr_before = total_psnr_before / processed_images
    avg_psnr_after = total_psnr_after / processed_images

    avg_ssim_before = total_ssim_before / processed_images
    avg_ssim_after = total_ssim_after / processed_images

    fps = processed_images / total_time

else:

    avg_psnr_before = 0
    avg_psnr_after = 0

    avg_ssim_before = 0
    avg_ssim_after = 0

    fps = 0

print("\nTesting Complete")

print(f"\nProcessed Images : {processed_images}")
print(f"Skipped Images   : {skipped_images}")

print(
    f"\nAverage PSNR : "
    f"{avg_psnr_before:.2f} -> "
    f"{avg_psnr_after:.2f}"
)

print(
    f"Average SSIM : "
    f"{avg_ssim_before:.4f} -> "
    f"{avg_ssim_after:.4f}"
)

print(f"\nFPS : {fps:.2f}")

print("\nSaved Results")
print(f"Enhanced : {IMG_DIR}")
print(f"Comparison : {COMPARE_DIR}")
print(f"CSV : {csv_path}")