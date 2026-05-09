# Hardware Deployment Workflow

## FPGA Deployment Overview

The repository includes an FPGA-compatible deployment model:

```text id="h4m8qx"
models/model_b8_c128_int.xmodel
```

The `.xmodel` file is a compiled INT8 deployment artifact generated using the Vitis AI workflow for DPU-oriented FPGA inference execution.

This deployment model can be directly executed on supported Xilinx FPGA platforms without requiring retraining or recompilation of the original PyTorch model.

The deployment workflow was validated using:

* Xilinx ZCU104 FPGA Board
* Vitis AI Runtime Environment
* INT8 Quantized Inference Pipeline
* DPU-Based Hardware Acceleration

---

# FPGA Deployment Procedure

## Step 1 — Prepare Deployment Files

Copy the required deployment files to a USB drive (pendrive).

Required files:

```text id="s2k7pv"
model_b8_c128_int.xmodel
test.py
input images
supporting inference files
```

---

# Step 2 — Connect FPGA Board

Connect the Xilinx ZCU104 board using:

* Ethernet connection
* USB/UART serial connection

The serial connection is used for runtime communication through PuTTY.

---

# Step 3 — Insert USB Drive into FPGA Board

Insert the USB drive containing the deployment files into the FPGA board.

---

# Step 4 — Open PuTTY Terminal

Open a PuTTY terminal session connected to the FPGA board.

After login, verify the connected USB device:

```bash id="d8q1mx"
lsblk
```

Create a mount directory:

```bash id="v5n4rz"
mkdir /mnt/usb
```

Mount the USB drive:

```bash id="u1k7tw"
mount /dev/sda1 /mnt/usb
```

---

# Step 5 — Copy Deployment Files

Copy deployment files from the mounted USB drive to the FPGA runtime directory:

```bash id="x3p8qy"
cp -r /mnt/usb/* ~/deployment/
```

Navigate to the deployment directory:

```bash id="g7m2vx"
cd ~/deployment
```

---

# Step 6 — Run FPGA Inference

Execute the hardware inference pipeline directly on the FPGA runtime environment.

The deployment workflow:

* loads the INT8 quantized `.xmodel`
* executes inference using the DPU
* processes degraded input images
* generates enhanced output images
* displays runtime execution logs and FPS measurements

---

# Hardware Inference Outputs

The FPGA-oriented inference workflow generates:

* enhanced output images
* runtime execution logs
* FPS measurements
* hardware acceleration results

Terminal execution screenshots included in this repository demonstrate successful FPGA deployment and runtime inference validation using the Xilinx ZCU104 platform.

---

# Deployment Notes

* The `.xmodel` file is hardware-ready for FPGA-oriented deployment workflows.
* No retraining is required for FPGA execution.
* Deployment files can be transferred directly using a USB drive.
* Hardware acceleration is achieved through DPU-based INT8 inference execution.
* The FPGA implementation demonstrates significantly faster inference performance compared to CPU-based execution workflows.
