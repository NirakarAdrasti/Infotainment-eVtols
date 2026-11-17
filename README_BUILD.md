# eVTOL Project - Complete Build & Run Guide

## ✅ BUILD STATUS: COMPLETE

All components have been built and configured successfully!

### Components Installed:
- ✓ **Python 3.12.3** - Main runtime
- ✓ **YOLOv8** - Object detection AI model
- ✓ **OpenCV (cv2)** - Computer vision library
- ✓ **NumPy** - Numerical computing
- ✓ **FastAPI** - Weather & Emergency backends
- ✓ **Uvicorn** - ASGI server
- ⚠️ **Node.js/npm** - Not installed (optional for React)

---

## 🚀 Quick Start

### Option A: Use the Menu (Easiest)
```bash
RUN.bat
```
Then select from the menu (1-7)

### Option B: Run Commands Directly

#### 1. **HTML Dashboard** (No server needed - direct file)
```bash
# Method 1: Open in browser directly
start home.html

# Method 2: Run on local server (recommended)
python -m http.server 8000
# Then open: http://localhost:8000/home.html
```

#### 2. **Object Detection** (with video)
```bash
python object_detection.py
```

#### 3. **Height/Altitude Detection**
```bash
python height_altitude.py
python height_detection.py
```

#### 4. **Weather API Backend**
```bash
cd jay_tiwari\backend
pip install -r requirements.txt
uvicorn main:app --reload
# Opens: http://localhost:8000
```

#### 5. **Emergency Procedure Backend**
```bash
cd "jay_tiwari\Emergency Procedure Prompts"
pip install -r requirements.txt
uvicorn app.main:app --reload
# opens: http://localhost:8000/ui
```

#### 6. **React Frontend** (requires Node.js)
```bash
cd "jay_tiwari\weather UI (react version2)"
npm install
npm run dev
# Opens: http://localhost:8080
```

#### 7. **Main Python Script**
```bash
python main.py
```

---

## 📁 Project Structure

```
eVTOL/
├── home.html              ✓ Flight Dashboard (WORKING)
├── object_detection.py    ✓ YOLOv8 Object Detection
├── height_altitude.py     ✓ Altitude Detection
├── height_detection.py    ✓ Height Detection
├── object_alert.py        ✓ Alert System
├── main.py               ✓ Main Entry Point
├── icon/                 ✓ All icons present
├── yolov8n.pt            ✓ AI Model (nano)
│
├── myenv/                ✓ Python Virtual Environment (activated)
│   ├── opencv-python     ✓ OpenCV
│   ├── ultralytics       ✓ YOLOv8
│   └── numpy             ✓ NumPy
│
└── jay_tiwari/
    ├── backend/                          ✓ Weather API
    │   ├── main.py                       ✓ FastAPI server
    │   ├── requirements.txt               ✓ Dependencies
    │   ├── airports.csv                  ✓ Airport data
    │   └── templates/index.html          ✓ Frontend
    │
    ├── Emergency Procedure Prompts/      ✓ Fault Detection
    │   ├── app/main.py                   ✓ FastAPI server
    │   ├── app/routes.py                 ✓ API endpoints
    │   ├── app/fault_logic.py            ✓ Fault detection
    │   ├── requirements.txt               ✓ Dependencies
    │   └── static/index.html             ✓ Frontend
    │
    └── weather UI (react version2)/      ⚠️ React (needs Node.js)
        ├── src/                          ✓ React components
        ├── package.json                  ✓ Dependencies
        ├── vite.config.ts                ✓ Build config
        └── backend/main.py               ✓ Python backend
```

---

## 🔧 Configuration

### Environment Variables

**Weather Backend** - `jay_tiwari/backend/.env`
```
OPENWEATHER_API_KEY=your_api_key_here
```
(Automatically created during setup)

### Port Mappings
| Service | Port | URL |
|---------|------|-----|
| HTML Dashboard | 8000 | http://localhost:8000/home.html |
| Weather API | 8000 | http://localhost:8000 |
| Emergency API | 8000 | http://localhost:8000/ui |
| React Frontend | 8080 | http://localhost:8080 |

---

## ✅ Testing & Verification

### Test Python Installation
```bash
python --version
```

### Test YOLOv8
```bash
python -c "from ultralytics import YOLO; print('YOLOv8 OK')"
```

### Test OpenCV
```bash
python -c "import cv2; print('OpenCV OK')"
```

### Test FastAPI
```bash
cd jay_tiwari\backend
uvicorn main:app --reload
# Check: http://localhost:8000/docs (API documentation)
```

---

## 🐛 Troubleshooting

### "Python not found"
- Install from https://www.python.org/
- Restart terminal after installation

### "Module not found: ultralytics, cv2, numpy"
- Ensure `myenv` is activated
- Run: `pip install ultralytics opencv-python numpy`

### "Port already in use"
- Kill existing process: `netstat -ano | findstr :8000`
- Or use different port: `python -m http.server 9000`

### "npm not recognized"
- Install Node.js from https://nodejs.org/
- React features will be unavailable until installed

### Video file not found
- Place video files in the root directory
- Update video_path in object_detection.py

---

## 📊 Status Summary

| Component | Status | Command |
|-----------|--------|---------|
| Python Runtime | ✓ OK | `python --version` |
| Virtual Environment | ✓ OK | `myenv\Scripts\activate.bat` |
| YOLOv8 | ✓ Installed | `python object_detection.py` |
| OpenCV | ✓ Installed | `python height_altitude.py` |
| FastAPI Backend 1 | ✓ Ready | `cd jay_tiwari\backend && uvicorn main:app --reload` |
| FastAPI Backend 2 | ✓ Ready | `cd jay_tiwari\Emergency Procedure Prompts && uvicorn app.main:app --reload` |
| HTML Dashboard | ✓ Working | `python -m http.server 8000` then open home.html |
| React Frontend | ⚠️ Needs Node.js | Install Node.js first |

---

## 🎯 Next Steps

1. ✓ Installation complete
2. **Run one of the backends** using commands above
3. **Open in browser** at the provided URLs
4. **Test the functionality** with your data
5. **(Optional) Install Node.js** to enable React features

---

**All systems ready!** Pick a component from the Quick Start section and run it now. 🚀
