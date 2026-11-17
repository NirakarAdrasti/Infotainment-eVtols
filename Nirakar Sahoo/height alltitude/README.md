# Flight Height & Altitude Detection System ✈️

This project is a **Flight Tracking & Infotainment System** that detects **height, altitude, and vertical speed** of aircrafts from video input.  
It integrates **computer vision (YOLOv8)** with a **Python backend** and a **web-based frontend** to visualize real-time tracking data.

---

## 🚀 Features
- Detect aircrafts in videos using **YOLOv8**.
- Measure **height, altitude, and vertical speed**.
- Overlay live flight data on the video (speed, altitude, time).
- Web-based dashboard with:
  - **Home Page** (`home.html`)
  - **Settings Page** (`setting.html`)
  - **Flight Tracking Display**.
- Backend Python scripts for object detection & data processing.
- Infotainment-like UI with:
  - Brightness Control  
  - Volume Control  
  - Battery Indicator  
  - Flight Statistics  

---

## 📂 Project Structure

```
project-root/
│── __pycache__/           # Python cache files
│── icon/                  # Icons for UI
│── myvenv/                # Virtual environment
│── VS Code.code-workspace # VS Code workspace config
│── allDetect.py           # Main detection runner
│── flight image.webp      # Flight UI image
│── flight_tracking.mp4    # Demo video output
│── height_altitude.py     # Altitude calculation logic
│── height_detection.py    # Height detection logic
│── home.css               # Frontend CSS
│── home.html              # Frontend homepage
│── main.py                # Entry point (backend + UI)
│── setting.html           # Settings page
│── utils.py               # Helper functions
│── verticalspeed.py       # Vertical speed calculations
│── video.mp4              # Input test video
│── video2.mp4             # Alternative test video
│── yolov8n.pt             # YOLOv8 model weights
```

---

## ⚙️ Installation

### 1. Clone Repository
```bash
git clone https://github.com/your-username/flight-height-altitude.git
cd flight-height-altitude
```

### 2. Setup Virtual Environment
```bash
python -m venv myvenv
source myvenv/bin/activate   # On Linux/Mac
myvenv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

*(create `requirements.txt` with necessary packages like `ultralytics`, `opencv-python`, `numpy`, `flask` etc.)*

---

## ▶️ Usage

### Run Detection
```bash
python main.py
```

### Run Specific Modules
- Height Detection:
```bash
python height_detection.py
```
- Altitude Detection:
```bash
python height_altitude.py
```
- Vertical Speed:
```bash
python verticalspeed.py
```

### Frontend
Open `home.html` in your browser for the dashboard UI.

---

## 🛠️ Tech Stack
- **Python** (backend processing)
- **YOLOv8** (aircraft detection)
- **OpenCV** (video analysis)
- **Flask / HTML / CSS / JS** (frontend dashboard)
- **VS Code** (development)

---

## 📸 Demo
- `video.mp4` → Input  
- `flight_tracking.mp4` → Output with overlayed height & altitude  

---

## 📌 Future Enhancements
- Add **real-time camera feed** integration.
- Improve UI with more infotainment features.
- Cloud storage for flight data history.

---

## 👨‍💻 Author
Developed by **Nirakar Sahoo**  
