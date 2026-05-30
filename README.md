# 🚀 FPGA Accelerated Image Enhancement using Quantization-Aware Residual CNN

<p align="center">
  <b>Real-Time FPGA Edge AI Pipeline for Low-Light Enhancement, Denoising, and Deblurring</b>
</p>

<p align="center">
  Residual CNN • INT8 Quantization • Vitis AI • DPU Acceleration • Edge AI
</p>

<p align="center">
  <a href="docs/Project_file.pdf">
    <img src="https://img.shields.io/badge/Project_Report-PDF-blue?style=for-the-badge">
  </a>
  <a href="docs/SOFTWARE_SETUP.md">
    <img src="https://img.shields.io/badge/Software_Deployment-Guide-success?style=for-the-badge">
  </a>
  <a href="docs/HARDWARE_SETUP.md">
    <img src="https://img.shields.io/badge/FPGA_Hardware-Setup-orange?style=for-the-badge">
  </a>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

---

# 📖 Overview

Most image enhancement systems are designed and benchmarked on GPUs. This project focuses on **FPGA-based deployment and acceleration** for real-time image restoration tasks.

The complete workflow integrates:

* Residual CNN Architecture
* Quantization-Aware Training (QAT)
* INT8 Optimization
* Xilinx Vitis AI Toolchain
* DPU Hardware Acceleration
* Docker-Based Deployment

The objective is to achieve **high-quality image enhancement with low latency and high power efficiency on edge devices**.

### Supported Enhancement Tasks

* 🔅 Low-Light Enhancement
* 🌫️ Image Denoising
* 🔍 Image Deblurring
* ⚡ INT8 Quantized Inference
* 🚀 FPGA Hardware Acceleration

---

# ✨ Key Features

| Component            | Implementation                   |
| -------------------- | -------------------------------- |
| Deep Learning Model  | Residual CNN                     |
| Quantization         | INT8 Quantization-Aware Training |
| FPGA Toolchain       | Xilinx Vitis AI                  |
| Hardware Accelerator | DPUCZDX8G                        |
| Deployment           | Docker + Native Runtime          |
| Evaluation           | PSNR & SSIM                      |
| Optimization         | Hardware-Aware Training          |
| Target Platform      | Xilinx ZCU104 FPGA               |

---

# 📊 Results & Performance

## Key Metrics at a Glance

| Metric                     | Value          |
| -------------------------- | -------------- |
| Software Average PSNR Gain | **+10.94 dB**  |
| Hardware Average PSNR Gain | **+9.71 dB**   |
| Average SSIM               | **0.90**       |
| FPGA Inference Speed       | **8.37 FPS**   |
| CPU Inference Speed        | 0.85 – 1.3 FPS |
| Speedup over CPU           | **≈ 8–10×**    |
| FPGA Power Consumption     | **≈ 5.1 W**    |
| Model Size (.xmodel)       | **≈ 3 MB**     |

---

## 📈 Software Results (FP32)

| Image ID    | Degraded PSNR | Enhanced PSNR | Gain       | Degraded SSIM | Enhanced SSIM |
| ----------- | ------------- | ------------- | ---------- | ------------- | ------------- |
| 91          | 14.41         | 26.36         | **+11.95** | 0.17          | 0.80          |
| 104         | 25.16         | 35.24         | **+10.08** | 0.58          | 0.95          |
| 133         | 22.13         | 32.92         | **+10.79** | 0.55          | 0.94          |
| **Average** | **20.57**     | **31.51**     | **+10.94** | **0.43**      | **0.90**      |

---

## 📈 Hardware Results (INT8 FPGA)

| Image ID    | Degraded PSNR | Enhanced PSNR | Gain       | Degraded SSIM | Enhanced SSIM |
| ----------- | ------------- | ------------- | ---------- | ------------- | ------------- |
| 30          | 22.10         | 31.45         | **+9.35**  | 0.62          | 0.89          |
| 37          | 20.85         | 30.92         | **+10.07** | 0.58          | 0.91          |
| **Average** | **21.48**     | **31.19**     | **+9.71**  | **0.60**      | **0.90**      |

> INT8 quantization introduces only **~1.23 dB PSNR reduction** compared to FP32 while delivering **8–10× faster inference**.

---

## ⚖️ Software vs Hardware Comparison

| Metric            | Software (FP32) | Hardware (INT8 FPGA) |
| ----------------- | --------------- | -------------------- |
| Precision         | FP32            | INT8                 |
| Avg PSNR Gain     | +10.94 dB       | +9.71 dB             |
| Avg SSIM          | 0.90            | 0.90                 |
| Inference Speed   | 0.85–1.3 FPS    | **8.37 FPS**         |
| Speedup           | 1×              | **8–10×**            |
| Model Size        | Full FP32       | ~4× Smaller          |
| Power Consumption | CPU             | **≈ 5.1 W**          |
| Deployment Target | CPU             | Xilinx ZCU104        |
| Accuracy Loss     | —               | ≈ −1.23 dB           |

---

## 🖥️ FPGA Runtime Validation

### PuTTY Serial Console Output

```text
COM15 - PuTTY  |  root@xilinx-zcu104-20222
Vitis AI 3.0 / DPU INT8
─────────────────────────────────────────────

980.png   | 30.59 → 37.94
981.png   | 36.43 → 36.61
982.png   | 20.34 → 31.11
984.png   | 30.10 → 30.00
985.png   | 29.40 → 31.16
987.png   | 10.16 → 30.88
99.png    | 32.58 → 37.42
993.png   | 26.62 → 26.65
996.png   | 31.96 → 32.52
999.png   | 36.53 → 37.71

FINAL SUMMARY

PSNR 20–25 dB → Avg Gain: +0.43 dB
PSNR 25–30 dB → Avg Gain: +0.67 dB
PSNR 30–35 dB → Avg Gain: +1.80 dB
PSNR 35–40 dB → Avg Gain: +0.49 dB

Overall Avg Gain: +1.21 dB

Time: 667.3 s for 5587 images
CSV saved:
results_final_1000.csv
```

### Hardware Throughput

* Total Images Processed: **5587**
* Execution Time: **667.3 s**
* Throughput: **8.37 FPS**
* Average Latency: **119.5 ms/frame**

---

# 🔧 FPGA Resource Utilization

**Platform:** Xilinx ZCU104 (XCZU7EV)
**DPU:** DPUCZDX8G B4096
**Toolchain:** Vitis AI 3.0

| Resource   | Used   | Available | Utilization   |
| ---------- | ------ | --------- | ------------- |
| LUTs       | 52,161 | 230,400   | 22.6%         |
| Flip-Flops | 98,249 | 460,800   | 21.3%         |
| DSP Slices | 710    | 1,728     | 41.1%         |
| UltraRAM   | 30     | 96        | 31.3%         |
| Block RAM  | 0      | 312       | UltraRAM Used |

---

## DPU Configuration

| Metric          | Value           |
| --------------- | --------------- |
| Architecture    | DPUCZDX8G B4096 |
| Parallelism     | 8 × 16 × 16     |
| Logic Clock     | 300 MHz         |
| DSP Clock       | 600 MHz         |
| Peak Throughput | 1,200 GOPS      |
| Precision       | INT8            |
| Inference Speed | 8.37 FPS        |
| Latency         | 119.5 ms        |
| Power           | 5.1 W           |
| Model Size      | ~3 MB           |

---

# 🏗 FPGA Deployment Workflow

```text
PyTorch Model
      │
      ▼
Quantization-Aware Training
      │
      ▼
INT8 Optimization
      │
      ▼
Vitis AI Compilation
      │
      ▼
.xmodel Generation
      │
      ▼
DPU Deployment
      │
      ▼
FPGA Inference
```

---

# 📂 Project Structure

```text
FPGA-Image-Enhancement/
│
├── models/
├── testing_code/
├── testing_images/
├── output/
├── results/
├── docs/
│   ├── Project_file.pdf
│   ├── SOFTWARE_SETUP.md
│   └── HARDWARE_SETUP.md
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 📊 Evaluation Metrics

### PSNR (Peak Signal-to-Noise Ratio)

Measures reconstruction quality between original and enhanced images.

**Higher PSNR = Better Image Restoration**

### SSIM (Structural Similarity Index)

Measures perceptual image quality and structural preservation.

**Higher SSIM = Better Visual Similarity**

---

# 🌍 Applications

* Smart Surveillance Systems
* Embedded Vision Systems
* Edge AI Platforms
* Robotics
* Autonomous Systems
* FPGA Research
* Real-Time Image Restoration
* Low-Light Imaging

---

# 🔮 Future Work

* [ ] Real-Time Video Enhancement
* [ ] INT4 Quantization
* [ ] Multi-DPU Scaling
* [ ] Streaming FPGA Inference
* [ ] Lightweight Edge AI Architectures
* [ ] Transformer-Based Restoration Networks

---

# 📄 License

MIT License

Copyright (c) 2026 Adeeb Ali

---

# 🙏 Acknowledgements

* AMD/Xilinx Vitis AI Ecosystem
* Xilinx FPGA Community
* PyTorch Framework
* Residual Learning Research Community
* Open-Source Edge AI Ecosystem

---


