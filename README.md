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

Most image enhancement systems are designed and benchmarked on GPUs. This project takes a different approach by focusing on **FPGA-based deployment and acceleration**.

The complete workflow is designed around Edge AI deployment using:

* Residual CNN Architecture
* Quantization-Aware Training (QAT)
* INT8 Optimization
* Xilinx Vitis AI Toolchain
* DPU Hardware Acceleration
* Docker-Based Deployment

The goal is to provide a practical FPGA image enhancement pipeline capable of delivering real-time performance while maintaining image quality.

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
| Hardware Accelerator | DPU                              |
| Deployment           | Docker + Native Runtime          |
| Evaluation           | PSNR & SSIM                      |
| Optimization         | Hardware-Aware Training          |
| Target Platform      | FPGA Edge AI Systems             |

---

# ⚡ Performance Matrix

| Metric            | CPU Execution  | FPGA DPU Execution |
| ----------------- | -------------- | ------------------ |
| Precision         | FP32           | INT8               |
| Inference Speed   | 0.85 – 1.3 FPS | 8.37 FPS           |
| Throughput Gain   | 1×             | 8–10× Faster       |
| Memory Usage      | High           | Reduced            |
| Deployment Target | CPU            | FPGA               |
| Power Efficiency  | Standard       | Improved           |

## Results

✅ Up to **10× faster inference**

✅ Reduced memory footprint through INT8 quantization

✅ FPGA-ready deployment pipeline

✅ Real-time Edge AI capability

✅ Maintained enhancement quality after quantization

---

# 🏗 FPGA Deployment & Hardware Acceleration

Unlike traditional CPU-based inference, this project deploys the optimized model directly onto FPGA hardware using the Xilinx Deep Processing Unit (DPU).

### Why FPGA?

* Low-Latency Inference
* Better Power Efficiency
* Hardware-Level Parallelism
* Customizable Acceleration
* Suitable for Embedded Systems
* Edge AI Friendly

### FPGA Deployment Workflow

```text
PyTorch Model
      │
      ▼
Quantization Aware Training
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

### Deployment Artifact

```text
models/model_b8_c128_int.xmodel
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

# 🐳 Running with Docker (Recommended)

Docker provides a reproducible environment for development and deployment.

## Build Docker Image

```bash
docker build -t fpga-enhancement .
```

## Run Container

```bash
docker run -it fpga-enhancement
```

### Docker Advantages

* Consistent Environment
* Easy Deployment
* Dependency Isolation
* Portable Execution
* Reproducible Results

---

# 💻 Manual Installation

## Clone Repository

```bash
git clone https://github.com/Adeeb-ali/FPGA-Accelerated-Image-Enhancement-using-Quantization-Aware-Residual-CNN.git

cd FPGA-Accelerated-Image-Enhancement-using-Quantization-Aware-Residual-CNN
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Inference

```bash
python testing_code/test.py
```

---

# 📚 Documentation & Deployment Guides

The repository contains detailed documentation covering the complete software and FPGA deployment workflow.

## 📄 Project Report

Complete project documentation including:

* Methodology
* Model Architecture
* Quantization Workflow
* FPGA Deployment Strategy
* Benchmark Results
* Evaluation Metrics
* Conclusions

```text
docs/Project_file.pdf
```

---

## 💻 Software Deployment Guide

The Software Deployment Guide contains:

* Environment Setup
* Python Dependencies
* Runtime Configuration
* Docker Workflow
* Vitis AI Software Setup
* Model Execution Procedures

```text
docs/SOFTWARE_SETUP.md
```

---

## 🏗 Hardware Deployment Guide

The Hardware Deployment Guide contains:

* FPGA Board Setup
* DPU Configuration
* Overlay Deployment
* Runtime Initialization
* Hardware Validation
* FPGA Inference Execution

```text
docs/HARDWARE_SETUP.md
```

---

# 🔬 Technical Architecture

## Residual CNN

Residual learning enables deeper neural networks while preserving image information and improving training stability.

### Benefits

* Faster Convergence
* Better Gradient Flow
* Improved Enhancement Quality
* Reduced Training Degradation

---

## Quantization-Aware Training (QAT)

QAT simulates INT8 arithmetic during training.

### Benefits

* FPGA-Compatible Models
* Reduced Accuracy Loss
* Lower Memory Consumption
* Faster Inference

---

## Vitis AI Deployment

The trained model is compiled using the Xilinx Vitis AI toolchain.

### Output

```text
.xmodel
```

The generated artifact can be executed directly by the FPGA DPU runtime.

---

## DPU Hardware Acceleration

The Deep Processing Unit (DPU) offloads CNN inference from the CPU and executes neural network operations directly on FPGA fabric.

### Advantages

* Reduced Latency
* Increased Throughput
* Better Power Efficiency
* Real-Time Processing

---

# 📊 Evaluation Metrics

## PSNR

Peak Signal-to-Noise Ratio measures reconstruction quality between original and enhanced images.

Higher values indicate better restoration quality.

---

## SSIM

Structural Similarity Index evaluates perceptual image quality and structural preservation.

Higher values indicate greater similarity to the reference image.

---

# 🌍 Applications

* Smart Surveillance Systems
* Edge AI Platforms
* Embedded Vision Systems
* Robotics
* Autonomous Systems
* FPGA Research
* Real-Time Image Restoration
* Low-Light Imaging

---

# 🛠 Troubleshooting

| Issue                | Solution                                    |
| -------------------- | ------------------------------------------- |
| Missing Dependencies | `pip install -r requirements.txt`           |
| Docker Not Installed | `docker --version`                          |
| FPGA Runtime Error   | Verify Vitis AI Runtime Installation        |
| DPU Issues           | Check Overlay and FPGA Configuration        |
| Slow CPU Inference   | Use FPGA Deployment for Real-Time Execution |

---

# 🔮 Future Work

* [ ] Real-Time Video Enhancement
* [ ] INT4 Quantization
* [ ] Streaming FPGA Inference
* [ ] Multi-Scale Restoration Networks
* [ ] Lightweight Edge AI Architectures
* [ ] Advanced Low-Light Reconstruction
* [ ] Multi-DPU Scaling

---

# 📄 License

MIT License

Copyright (c) 2026 Adeeb Ali

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction.

---

# 🙏 Acknowledgements

* Xilinx Vitis AI Ecosystem
* AMD/Xilinx FPGA Community
* PyTorch Framework
* Residual Learning Research Community
* Open-Source Edge AI Ecosystem

---

<p align="center">
  <b>Built for FPGA Acceleration • Edge AI • Real-Time Image Enhancement</b>
</p>
