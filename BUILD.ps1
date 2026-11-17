#!/usr/bin/env pwsh

Write-Host ""
Write-Host "========================================"  -ForegroundColor Cyan
Write-Host "   eVTOL Project Setup and Build Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "[1/7] Checking Python..." -ForegroundColor Yellow
$pythonCheck = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Python found: $pythonCheck" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Python not installed!" -ForegroundColor Red
    Write-Host "Download from: https://www.python.org/" -ForegroundColor Yellow
    exit 1
}

# Setup Python environment
Write-Host "`n[2/7] Creating Python virtual environment..." -ForegroundColor Yellow
if (Test-Path "myenv") {
    Write-Host "[OK] Virtual environment already exists" -ForegroundColor Green
} else {
    python -m venv myenv
    Write-Host "[OK] Virtual environment created" -ForegroundColor Green
}

# Activate
& "myenv\Scripts\Activate.ps1"

# Install root dependencies
Write-Host "`n[3/7] Installing Python packages..." -ForegroundColor Yellow
pip install -q --upgrade pip setuptools wheel
pip install -q ultralytics opencv-python numpy
Write-Host "[OK] Python packages installed (YOLOv8, OpenCV, NumPy)" -ForegroundColor Green

# Setup FastAPI backends
Write-Host "`n[4/7] Setting up FastAPI backends..." -ForegroundColor Yellow

Push-Location "jay_tiwari\backend"
if (-not (Test-Path ".env")) {
    Set-Content ".env" "OPENWEATHER_API_KEY=your_api_key_here"
}
pip install -q -r requirements.txt
Pop-Location
Write-Host "[OK] Weather Backend configured" -ForegroundColor Green

Push-Location "jay_tiwari\Emergency Procedure Prompts"
pip install -q -r requirements.txt
Pop-Location
Write-Host "[OK] Emergency Procedure Backend configured" -ForegroundColor Green

# Check Node.js
Write-Host "`n[5/7] Checking Node.js..." -ForegroundColor Yellow
$nodeCheck = node --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Node.js found: $nodeCheck" -ForegroundColor Green
} else {
    Write-Host "[WARNING] Node.js not installed - skipping React setup" -ForegroundColor Yellow
    Write-Host "Download from: https://nodejs.org/" -ForegroundColor Yellow
    goto Skip_React
}

# Setup React
Write-Host "`n[6/7] Setting up React Frontend..." -ForegroundColor Yellow
Push-Location "jay_tiwari\weather UI (react version2)"
if (-not (Test-Path "node_modules")) {
    npm install -q
    Write-Host "[OK] React dependencies installed" -ForegroundColor Green
} else {
    Write-Host "[OK] React dependencies already present" -ForegroundColor Green
}
Pop-Location

:Skip_React

Write-Host "`n[7/7] Build Complete!" -ForegroundColor Green
Write-Host ""
Write-Host "========================================"  -ForegroundColor Cyan
Write-Host "   Setup Complete - Ready to Run!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "COMMAND QUICK REFERENCE:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. HTML Dashboard:" -ForegroundColor White
Write-Host "   python -m http.server 8000" -ForegroundColor Cyan
Write-Host "   Open: http://localhost:8000/home.html" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. Object Detection:" -ForegroundColor White
Write-Host "   python object_detection.py" -ForegroundColor Cyan
Write-Host ""
Write-Host "3. Weather API (http://localhost:8000):" -ForegroundColor White
Write-Host "   cd jay_tiwari\backend && uvicorn main:app --reload" -ForegroundColor Cyan
Write-Host ""
Write-Host "4. Emergency Backend (http://localhost:8000):" -ForegroundColor White
Write-Host "   cd 'jay_tiwari\Emergency Procedure Prompts'" -ForegroundColor Cyan
Write-Host "   uvicorn app.main:app --reload" -ForegroundColor Cyan
Write-Host ""
Write-Host "5. React Dev Server (http://localhost:8080):" -ForegroundColor White
Write-Host "   cd 'jay_tiwari\weather UI (react version2)' && npm run dev" -ForegroundColor Cyan
Write-Host ""
Write-Host "6. React Production Build:" -ForegroundColor White
Write-Host "   cd 'jay_tiwari\weather UI (react version2)' && npm run build" -ForegroundColor Cyan
Write-Host ""
Write-Host "========================================"  -ForegroundColor Cyan
Write-Host ""
