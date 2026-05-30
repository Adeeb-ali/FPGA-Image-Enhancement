# 🚀 FPGA Edge AI Image Enhancement

<p align="center">
  <b>Real-Time Image Enhancement on FPGA using Residual CNNs, INT8 Quantization, and Xilinx Vitis AI</b>
</p>

<p align="center">
  Low-Light Restoration • Denoising • Deblurring • Hardware Accelerated Inference
</p>

---

## 📖 Overview

This project demonstrates a complete FPGA-oriented image enhancement pipeline built for real-time Edge AI deployment.

Unlike traditional image enhancement systems that rely on GPUs, this implementation is optimized specifically for FPGA hardware using:

* Residual CNN Architecture
* INT8 Quantization-Aware Training (QAT)
* Xilinx Vitis AI Toolchain
* DPU Hardware Acceleration
* Docker-Based Deployment

The system enhances degraded images while achieving significantly faster inference through FPGA acceleration.

---

## ✨ Key Features

* 🔅 Low-Light Enhancement
* 🌫️ Image Denoising
* 🔍 Deblurring
* ⚡ INT8 Quantized Inference
* 🚀 FPGA DPU Deployment
* 📊 PSNR & SSIM Evaluation
* 🐳 Docker Support
* 🔧 Vitis AI Integration

---

# ⚡ Performance Matrix

| Metric            | CPU Execution | FPGA DPU Execution     |
| ----------------- | ------------- | ---------------------- |
| Precision         | FP32          | INT8                   |
| Inference Speed   | 0.85–1.3 FPS  | 8.37 FPS               |
| Throughput Gain   | 1×            | 8–10× Faster           |
| Power Efficiency  | Standard      | Significantly Improved |
| Deployment Target | CPU           | FPGA                   |

### Results

✅ Up to 10× faster inference

✅ Reduced memory footprint through INT8 quantization

✅ Real-time deployment capability

✅ Maintained enhancement quality after quantization

---

# 🏗 Why FPGA?

Field-Programmable Gate Arrays (FPGAs) provide a balance between performance, flexibility, and power efficiency.

### Advantages

* Lower latency than CPU inference
* Better power efficiency than many GPU deployments
* Customizable hardware acceleration
* Suitable for embedded systems
* Ideal for Edge AI applications

### FPGA Workflow

PyTorch Model
↓
Quantization Aware Training
↓
INT8 Optimization
↓
Vitis AI Compilation
↓
.xmodel Generation
↓
DPU Deployment
↓
FPGA Inference

Deployment Artifact:

models/model_b8_c128_int.xmodel

---

# 📂 Project Structure

FPGA-Image-Enhancement/

├── models/

├── testing_code/

├── testing_images/

├── output/

├── results/

├── docs/

├── Dockerfile

├── requirements.txt

└── README.md

---

# 🐳 Running with Docker (Recommended)

## Build Image

```bash
docker build -t fpga-enhancement .
```

## Run Container

```bash
docker run -it fpga-enhancement
```

### Benefits

* Consistent environment
* Easy deployment
* Dependency isolation
* Faster setup

---

# 💻 Manual Installation

## Clone Repository

```bash
git clone https://github.com/your-username/FPGA-Image-Enhancement.git

cd FPGA-Image-Enhancement
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

# 🔬 Technical Architecture

## Residual CNN

Residual learning improves convergence stability while preserving image information.

## Quantization-Aware Training

QAT simulates INT8 arithmetic during training, minimizing post-quantization accuracy loss.

## Vitis AI Deployment

The trained network is compiled into FPGA-ready .xmodel artifacts for DPU execution.

## DPU Acceleration

The Deep Processing Unit executes CNN inference directly on FPGA fabric, improving throughput and reducing latency.

---

# 📊 Evaluation Metrics

### PSNR

Measures reconstruction quality between original and enhanced images.

### SSIM

Measures perceptual similarity and structural preservation.

---

# 🌍 Applications

* Smart Surveillance
* Edge AI Systems
* Robotics
* Autonomous Platforms
* Real-Time Image Restoration
* FPGA Research

---

# 🔮 Future Work

* Real-Time Video Enhancement
* INT4 Quantization
* Streaming FPGA Inference
* Lightweight Edge AI Models
* Multi-Scale Restoration Networks

---

# 📄 License

MIT License

Copyright (c) 2026 Adeeb Ali

---

# 🙏 Acknowledgements

* Xilinx Vitis AI
* PyTorch
* FPGA Open-Source Community
* Edge AI Research Community
