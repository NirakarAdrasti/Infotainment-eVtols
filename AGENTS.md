# eVTOL Project - Agent Instructions

This is an **eVTOL (Electric Vertical Takeoff and Landing) aircraft monitoring system** with multiple components: object detection pipelines, flight monitoring backends, emergency procedure systems, and weather dashboards.

## 🏗️ Project Architecture

```
┌─ Root Level Python Scripts
│  ├─ Object Detection (YOLOv8-based)
│  ├─ Height/Altitude Detection
│  └─ Vertical Speed Tracking
│
└─ jay_tiwari/ (Main development folder)
   ├─ backend/ (FastAPI - Airport Weather Streaming)
   ├─ Emergency Procedure Prompts/ (FastAPI - Fault Detection)
   └─ weather UI (react version2)/ (Vite+React+FastAPI)
```

## 🚀 Quick Start Commands

### Python Virtual Environments
```bash
# Activate myenv (primary environment with CV2, NumPy)
cd c:\Users\DELL\Desktop\New folder
source myenv/Scripts/activate  # or: myenv\Scripts\activate.bat (Windows)

# Activate myvenv (lightweight environment)
source myvenv/Scripts/activate
```

### Root Level Python Scripts
```bash
# Object detection from video
python object_detection.py

# Height/altitude detection
python height_detection.py
python height_altitude.py

# Run main application
python main.py
```

### FastAPI Backends

**Weather/Airport Backend** (`jay_tiwari/backend/`)
```bash
cd jay_tiwari/backend
pip install -r requirements.txt
uvicorn main.py --reload  # Runs on http://localhost:8000
# Streams real-time weather for airports (requires OPENWEATHER_API_KEY in .env)
```

**Emergency Procedure System** (`jay_tiwari/Emergency Procedure Prompts/`)
```bash
cd jay_tiwari/Emergency Procedure Prompts
pip install -r requirements.txt
uvicorn app.main:app --reload  # Runs on http://localhost:8000
# API endpoint: /ui for frontend
```

### React + FastAPI Stack

**Weather UI (React + Vite)** (`jay_tiwari/weather UI (react version2)/`)

**Development:**
```bash
cd "jay_tiwari/weather UI (react version2)"
npm install
npm run dev      # Frontend runs on http://localhost:8080
```

In another terminal, start the Python backend:
```bash
cd "jay_tiwari/weather UI (react version2)/backend"
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Production:**
```bash
npm run build        # Creates dist/ folder
npm run preview      # Preview production build locally
```

**Maintenance:**
```bash
npm run lint         # Check code style (ESLint)
npm run build:dev    # Build with development configuration
```

## 📦 Key Dependencies

### Root Python Scripts
- **ultralytics** (YOLOv8 for object detection)
- **opencv-python** (CV2 for video processing)
- **numpy** (numerical computing)

### FastAPI Backends
- **fastapi** - Web framework
- **uvicorn** - ASGI server
- **httpx** - Async HTTP client (for weather API calls)
- **python-dotenv** - Environment variable management

### React Frontend
- **Vite** - Build tool and dev server
- **React 18** - UI framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **shadcn/ui + Radix UI** - Component library
- **React Router** - Client-side routing
- **Recharts** - Data visualization
- **React Hook Form + Zod** - Form handling

## 🔧 Project Structure Details

### Root Level
- `main.py` - Main entry point
- `object_detection.py` - YOLOv8-based object detector
- `height_detection.py`, `height_altitude.py` - Altitude tracking
- `object_alert.py`, `allDetect.py` - Alert and aggregation systems
- `yolov8n.pt` - YOLOv8 nano model weights
- `myenv/` - Primary Python environment (CV2, NumPy, YOLOv8)
- `home.html`, `phone.html`, `setting.html` - Web frontends
- `Nirakar Sahoo/`, `Gopal_eVTOL/` - Team member subfolders

### jay_tiwari/
- `backend/` - FastAPI airport weather service
  - `main.py` - Entry point
  - `requirements.txt` - Dependencies
  - `airports.csv` - Airport dataset
  - `templates/index.html` - Frontend UI

- `Emergency Procedure Prompts/` - Fault detection system
  - `app/main.py` - FastAPI application
  - `app/routes.py` - API endpoints
  - `app/fault_logic.py` - Fault detection logic
  - `static/index.html` - Frontend

- `weather UI (react version2)/` - Modern React dashboard
  - `src/` - React components and pages
  - `backend/main.py` - Python backend
  - `vite.config.ts` - Build configuration
  - `tailwind.config.ts` - Styling configuration

## 🔌 Environment Variables

**Weather Backend** (`.env`)
```
OPENWEATHER_API_KEY=your_api_key_here
```

**React App** (`.env` in `weather UI (react version2)/`)
```
VITE_API_URL=http://localhost:8000
```

## 🐛 Common Development Issues

1. **ModuleNotFoundError: cv2**
   - Ensure `myenv` is activated (has opencv-python installed)
   - Root scripts require CV2; use `myenv` not `myvenv`

2. **Port Already in Use**
   - FastAPI defaults to 8000
   - React Vite defaults to 8080
   - Specify custom ports: `uvicorn main.py --port 8001` or adjust vite.config.ts

3. **CORS Issues with React + FastAPI**
   - Backends include CORS middleware configured for localhost
   - Check `allow_origins` in FastAPI app configuration

4. **Missing airports.csv**
   - Download from [OurAirports](https://ourairports.com/data/)
   - Place in `jay_tiwari/backend/` root directory

## 📝 Common Tasks

### Running the full stack
```bash
# Terminal 1: React frontend
cd "jay_tiwari/weather UI (react version2)"
npm run dev

# Terminal 2: Python backend
cd "jay_tiwari/weather UI (react version2)/backend"
source activate_myenv.sh  # or equivalent
uvicorn main:app --reload --port 8000
```

### Building for production
```bash
cd "jay_tiwari/weather UI (react version2)"
npm run build
```

### Running object detection on video
```bash
cd c:\Users\DELL\Desktop\New folder
source myenv/Scripts/activate
python object_detection.py
```

## 📚 Key Files for AI Agents

- Build/Run entry points: See **Quick Start Commands** above
- Package configs: `package.json`, `requirements.txt` files
- Main logic: `main.py` files in each service
- Configuration: `vite.config.ts`, `tailwind.config.ts`

## ✅ Before Starting Development

1. Activate appropriate Python environment (`myenv` for CV2, `myvenv` for lightweight)
2. Install dependencies: `pip install -r requirements.txt` or `npm install`
3. Configure environment variables (`.env` files)
4. For React app: ensure Node.js 16+ is installed
5. For FastAPI: ensure Python 3.8+ is installed
