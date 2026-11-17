@echo off
REM ============================================
REM eVTOL Project - Complete Setup & Build
REM ============================================

echo.
echo ========================================
echo   eVTOL Project Setup & Build Script
echo ========================================
echo.

REM Check Python
echo [1/8] Checking Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)
echo ✓ Python found

REM Setup Root Python Environment
echo.
echo [2/8] Setting up root Python environment...
if not exist "myenv\Scripts\activate.bat" (
    python -m venv myenv
    echo ✓ Virtual environment created
)
call myenv\Scripts\activate.bat
pip install --upgrade pip setuptools wheel >nul 2>&1
echo ✓ Root environment ready

REM Install Root Dependencies
echo.
echo [3/8] Installing root Python dependencies...
pip install ultralytics opencv-python numpy -q
echo ✓ Root dependencies installed (YOLOv8, OpenCV, NumPy)

REM Setup FastAPI Backend - Weather
echo.
echo [4/8] Setting up Weather Backend (FastAPI)...
cd jay_tiwari\backend
if not exist ".env" (
    echo OPENWEATHER_API_KEY=your_api_key_here > .env
    echo ✓ Created .env (add your API key)
)
pip install -r requirements.txt -q
cd ..\..
echo ✓ Weather Backend ready

REM Setup FastAPI Backend - Emergency Procedure
echo.
echo [5/8] Setting up Emergency Procedure Backend (FastAPI)...
cd "jay_tiwari\Emergency Procedure Prompts"
pip install -r requirements.txt -q
cd ..\..
echo ✓ Emergency Procedure Backend ready

REM Check Node.js
echo.
echo [6/8] Checking Node.js...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo WARNING: Node.js not found!
    echo Install from: https://nodejs.org/
    echo Skipping React build...
    goto skip_react
)
echo ✓ Node.js found

REM Setup React App
echo.
echo [7/8] Setting up React Frontend (Vite)...
cd "jay_tiwari\weather UI (react version2)"
if not exist "node_modules" (
    npm install -q
    echo ✓ React dependencies installed
) else (
    echo ✓ React dependencies already installed
)
cd ..\..
echo ✓ React Frontend ready

:skip_react

REM All done
echo.
echo [8/8] Build Complete!
echo.
echo ========================================
echo   ✓ All Components Ready to Run
echo ========================================
echo.
echo QUICK START COMMANDS:
echo.
echo 1. Run HTML Dashboard (Open in browser):
echo    python -m http.server 8000
echo    Then open: http://localhost:8000/home.html
echo.
echo 2. Run Object Detection:
echo    python object_detection.py
echo.
echo 3. Run Weather Backend:
echo    cd jay_tiwari\backend
echo    uvicorn main:app --reload
echo.
echo 4. Run Emergency Procedure Backend:
echo    cd "jay_tiwari\Emergency Procedure Prompts"
echo    uvicorn app.main:app --reload
echo.
echo 5. Run React Frontend (Dev):
echo    cd "jay_tiwari\weather UI (react version2)"
echo    npm run dev
echo.
echo 6. Build React (Production):
echo    cd "jay_tiwari\weather UI (react version2)"
echo    npm run build
echo.
echo ========================================
echo.
pause
