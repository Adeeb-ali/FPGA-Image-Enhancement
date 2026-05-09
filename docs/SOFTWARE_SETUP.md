# Software Setup Guide

This document explains two methods for running the image enhancement pipeline:

1. Manual Python-Based Setup
2. Docker-Based Setup

The implementation uses the trained residual CNN model:

```text id="f7m2qx"
models/best_model_arch1.pth
```

The inference pipeline automatically:

* loads the trained model
* processes degraded PNG input images
* generates enhanced outputs
* creates output directories automatically during execution

---

# Python Version

The project was developed and tested using:

```text id="k4v8pr"
Python 3.10
```

Using different Python versions may require additional dependency adjustments.

---

# 1. Manual Python-Based Setup

## Step 1 — Navigate to Project Directory

```bash id="u5n1qx"
cd /Users/adeebsmac/results-images-enhacement
```

---

## Step 2 — Verify Python Version

```bash id="r8m4tw"
python3 --version
```

Expected output:

```text id="j2k7pv"
Python 3.10
```

---

## Step 3 — Install Dependencies

```bash id="v6q9rx"
pip install -r requirements.txt
```

---

## Step 4 — Prepare Input Images

Place degraded PNG input images inside:

```text id="n3m8vz"
testing_images/degraded/
```

Optional ground truth reference images may be stored inside:

```text id="d7k2qx"
testing_images/clean/
```

---

## Step 5 — Navigate to Testing Directory

```bash id="t1v4pr"
cd testing_code
```

---

## Step 6 — Run Inference

```bash id="x8m2qw"
python test.py
```

Enhanced output images are automatically generated and saved inside:

```text id="c5k9rx"
output/
```

---

# 2. Docker-Based Setup

## Step 1 — Navigate to Project Directory

```bash id="m4v7tw"
cd /Users/adeebsmac/results-images-enhacement
```

---

## Step 2 — Build Docker Image

```bash id="q2k8pr"
docker build -t image-enhancement .
```

This command creates a reusable Docker execution environment containing:

* Python 3.10
* PyTorch
* OpenCV
* required project dependencies

---

## Step 3 — Prepare Input Images

Create a local folder containing degraded PNG input images.

Example:

```text id="g6m1qx"
images/
   ├── image1.png
   ├── image2.png
   └── image3.png
```

---

## Step 4 — Run Docker Container

```bash id="w9k4pv"
docker run -it --rm \
-v $(pwd)/images:/input \
-v $(pwd)/results:/output \
image-enhancement \
--input /input \
--output /output
```

---

## Docker Volume Mapping

| Local System     | Docker Container |
| ---------------- | ---------------- |
| `$(pwd)/images`  | `/input`         |
| `$(pwd)/results` | `/output`        |

Input images are read from:

```text id="p3m7rx"
/input
```

Enhanced output images are automatically saved inside:

```text id="u1k8tw"
/output
```

The generated output images will also appear automatically inside the local:

```text id="r5v2qx"
results/
```

directory on the host machine.

This workflow provides a reproducible Docker-based inference environment while preserving local project files and generated outputs.
