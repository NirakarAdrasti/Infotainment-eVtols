@echo off
REM Simple menu for running eVTOL project components

:menu
cls
echo.
echo ========================================
echo   eVTOL PROJECT - RUN MENU
echo ========================================
echo.
echo [1] Run HTML Dashboard (http://localhost:8000)
echo [2] Run Object Detection
echo [3] Run Weather API Backend (http://localhost:8000)
echo [4] Run Emergency Procedure Backend (http://localhost:8000)
echo [5] Run React Frontend (http://localhost:8080)
echo [6] Run Python Main Script
echo [7] Exit
echo.
set /p choice="Enter your choice (1-7): "

if "%choice%"=="1" goto dashboard
if "%choice%"=="2" goto detection
if "%choice%"=="3" goto weather
if "%choice%"=="4" goto emergency
if "%choice%"=="5" goto react
if "%choice%"=="6" goto mainscript
if "%choice%"=="7" goto exit
echo Invalid choice. Please try again.
goto menu

:dashboard
echo Starting HTML Dashboard...
echo Activating environment...
call myenv\Scripts\activate.bat
python -m http.server 8000
goto menu

:detection
echo Starting Object Detection...
call myenv\Scripts\activate.bat
python object_detection.py
goto menu

:weather
echo Starting Weather Backend...
cd jay_tiwari\backend
call ..\..\myenv\Scripts\activate.bat
pip install -q -r requirements.txt
uvicorn main:app --reload
cd ..\..
goto menu

:emergency
echo Starting Emergency Procedure Backend...
cd "jay_tiwari\Emergency Procedure Prompts"
call "..\..\myenv\Scripts\activate.bat"
pip install -q -r requirements.txt
uvicorn app.main:app --reload
cd ..\..
goto menu

:react
echo Starting React Frontend...
cd "jay_tiwari\weather UI (react version2)"
call "..\..\myenv\Scripts\activate.bat"
npm run dev
cd ..\..
goto menu

:mainscript
echo Starting Main Python Script...
call myenv\Scripts\activate.bat
python main.py
goto menu

:exit
echo Goodbye!
