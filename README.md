<div align="center">

# 🚦 ASTRo
### Assurance of Safety for Transport and Road Operations

*An AI-powered, edge-deployed road safety system using real-time computer vision*

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFAA?style=flat-square)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-4B-C51A4A?style=flat-square&logo=raspberry-pi&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat-square&logo=opencv&logoColor=white)

</div>

---

## Overview

ASTRo is a real-time road safety monitoring system that runs entirely on a Raspberry Pi. It uses computer vision and deep learning to detect pedestrians, vehicles, and animals on roads — and immediately triggers physical alerts to warn drivers before accidents happen.

Designed for environments where existing infrastructure fails: mountain highways, forest roads, fog-prone corridors, unmonitored crossings, and wildlife zones.

---

## The Problem

Road systems are inherently unpredictable. Standard passive safety measures cannot respond dynamically to:

- 🚶 **Jaywalking** and unauthorized pedestrian crossings
- 🐾 **Wildlife** entering highways in forest and mountain regions
- 🌫️ **Low-visibility conditions** — fog, night-time, sharp bends
- 🚗 **Delayed driver reaction** to sudden road hazards
- 🏔️ **Accident-prone roads** with no active monitoring

ASTRo addresses these gaps with always-on, edge-deployed detection and instant physical alerting — no cloud dependency, no latency.

---

## Features

| Feature | Description |
|---|---|
| 🎥 Real-time Object Detection | YOLOv8n inference on live camera feed |
| 🧠 Multi-class Classification | Detects humans, animals, and vehicles |
| 💡 GPIO LED Alert System | Instant physical warning signal on detection |
| 📺 Live Camera Feed Processing | Continuous frame-by-frame analysis via Picamera2 |
| 🎞️ Video Recording | Saves footage with detection bounding boxes overlaid |
| ☁️ Auto Cloud Backup | Uploads recordings to Google Drive via rclone |
| ⚡ Edge Deployment | Fully offline — no internet required for core operation |

---

## Hardware

| Component | Purpose |
|---|---|
| Raspberry Pi 4B | Central processing unit |
| Raspberry Pi Camera Module 3 | Real-time video capture |
| Breadboard | Circuit prototyping |
| LED | Visual alert indicator |
| 220Ω Resistor | LED current limiting |
| Jumper Wires | GPIO connections |

---

## Software Stack

| Tool | Role |
|---|---|
| Python | Core application logic |
| YOLOv8n (Ultralytics) | Object detection model |
| OpenCV | Frame processing and annotation |
| Picamera2 | Camera interface for Raspberry Pi |
| RPi.GPIO | LED control via GPIO pins |
| rclone | Automated Google Drive upload |

---

## System Architecture
```
                        ┌──────────────────────────────────┐
                        │         Raspberry Pi 4B          │
                        │                                  │
   ┌──────────────────┐ │  ┌─────────────────────────────┐ │
   │  Camera Module 3 │─┼─▶│      Picamera2 Capture      │ │
   └──────────────────┘ │  └──────────────┬──────────────┘ │
                        │                 │                 │
                        │                 ▼                 │
                        │  ┌──────────────────────────────┐ │
                        │  │       YOLOv8n Inference      │ │
                        │  └───────┬──────────┬───────────┘ │
                        │          │          │          │  │
                        │          ▼          ▼          ▼  │
                        │  ┌──────────┐ ┌─────────┐ ┌─────┐│
                        │  │ GPIO LED │ │  OpenCV │ │rclone││
                        │  │  Alert   │ │  Record │ │Upload││
                        │  └──────────┘ └─────────┘ └─────┘│
                        └──────────────────────────────────┘
```

**Flow:**
1. Camera captures live road footage continuously
2. YOLOv8n classifies objects frame-by-frame (humans, animals, vehicles)
3. On hazard detection → GPIO LED triggers instantly
4. OpenCV annotates and saves the recording with bounding boxes
5. rclone uploads the footage to Google Drive automatically

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ASTRo.git
cd ASTRo
```

### 2. Install Dependencies

```bash
pip install ultralytics opencv-python picamera2 RPi.GPIO
```

### 3. Install rclone (for Google Drive upload)

```bash
curl https://rclone.org/install.sh | sudo bash
rclone config
```

### 4. Connect Hardware

- Connect LED to GPIO pin (default: GPIO 17) with a 220Ω resistor to GND
- Attach Raspberry Pi Camera Module via CSI ribbon cable
- Enable the camera interface: `sudo raspi-config` → Interface Options → Camera

### 5. Run ASTRo

```bash
python astro.py
```

---

## Configuration

Edit the config section in `astro.py` to adjust:

```python
GPIO_PIN      = 17
CONFIDENCE    = 0.5
RECORD        = True
UPLOAD        = True
DRIVE_REMOTE  = "gdrive:ASTRo_Recordings"
```

---

## Target Environments

- Urban pedestrian crossings with frequent jaywalking
- Forest and wildlife corridor roads
- Mountain and highland highways with sharp curves
- Low-visibility zones (fog, night, tunnel exits)
- Unmonitored rural road stretches

---

## Design Approach

| Approach | Evaluated | Outcome |
|---|---|---|
| Infrared Sensors | ✓ | Limited to heat signatures; no object classification |
| Ultrasonic Sensors | ✓ | Proximity-only; no tracking or multi-object support |
| **Camera + CV** | ✓ ✅ | Selected — best tracking, classification, and scalability |

---

## Roadmap

- [ ] Multi-camera support
- [ ] SMS/IoT alert integration
- [ ] Dashboard for remote monitoring
- [ ] Custom model training for region-specific wildlife
- [ ] Integration with traffic signal systems

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push and open a Pull Request

---

<div align="center">
  <sub>Built with 🔴 on Raspberry Pi — keeping roads safer, one frame at a time.</sub>
</div>
