# ============================================
# eVTOL Project - Complete Setup & Build
# ============================================

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "   eVTOL Project Setup & Build Script" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Step 1: Check Python
Write-Host "[1/8] Checking Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[OK] Python found: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "ERROR: Python not found!" -ForegroundColor Red
    Write-Host "Please install Python 3.8+ from https://www.python.org/" -ForegroundColor Red
    exit
}

# Step 2: Setup Root Python Environment
Write-Host "`n[2/8] Setting up root Python environment..." -ForegroundColor Yellow
if (-not (Test-Path "myenv\Scripts\activate.ps1")) {
    python -m venv myenv | Out-Null
    Write-Host "[OK] Virtual environment created" -ForegroundColor Green
}
else {
    Write-Host "[OK] Virtual environment already exists" -ForegroundColor Green
}

# Activate venv
& "myenv\Scripts\Activate.ps1"
python -m pip install --upgrade pip setuptools wheel -q
Write-Host "[OK] Root environment ready" -ForegroundColor Green

# Step 3: Install Root Dependencies
Write-Host "`n[3/8] Installing root Python dependencies..." -ForegroundColor Yellow
pip install ultralytics opencv-python numpy -q
Write-Host "[OK] Root dependencies installed (YOLOv8, OpenCV, NumPy)" -ForegroundColor Green

# Step 4: Setup FastAPI Backend - Weather
Write-Host "`n[4/8] Setting up Weather Backend (FastAPI)..." -ForegroundColor Yellow
Push-Location "jay_tiwari\backend"
if (-not (Test-Path ".env")) {
    "OPENWEATHER_API_KEY=your_api_key_here" | Out-File -FilePath ".env" -Encoding UTF8
    Write-Host "[OK] Created .env (add your API key)" -ForegroundColor Green
}
pip install -r requirements.txt -q
Pop-Location
Write-Host "[OK] Weather Backend ready" -ForegroundColor Green

# Step 5: Setup FastAPI Backend - Emergency Procedure
Write-Host "`n[5/8] Setting up Emergency Procedure Backend (FastAPI)..." -ForegroundColor Yellow
Push-Location "jay_tiwari\Emergency Procedure Prompts"
pip install -r requirements.txt -q
Pop-Location
Write-Host "[OK] Emergency Procedure Backend ready" -ForegroundColor Green

# Step 6: Check Node.js
Write-Host "`n[6/8] Checking Node.js..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version 2>&1
    Write-Host "[OK] Node.js found: $nodeVersion" -ForegroundColor Green
}
catch {
    Write-Host "WARNING: Node.js not found!" -ForegroundColor Yellow
    Write-Host "Install from: https://nodejs.org/" -ForegroundColor Yellow
    Write-Host "Skipping React setup..." -ForegroundColor Yellow
    $skipReact = $true
}

# Step 7: Setup React App
if (-not $skipReact) {
    Write-Host "`n[7/8] Setting up React Frontend (Vite)..." -ForegroundColor Yellow
    Push-Location "jay_tiwari\weather UI (react version2)"
    if (-not (Test-Path "node_modules")) {
        npm install [OK] React dependencies installed" -ForegroundColor Green
    }
    else {
        Write-Host "[OK] React dependencies already installed" -ForegroundColor Green
    }
    Pop-Location
    Write-Host "[OK] React Frontend ready" -ForegroundColor Green
}
else {
    Write-Host "[7/8] Skipping React setup" -ForegroundColor Yellow
}

# All done
Write-Host "`n[8/8] Build Complete!" -ForegroundColor Green
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "   [OK]======================================" -ForegroundColor Cyan
Write-Host "   ✓ All Components Ready to Run" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "QUICK START COMMANDS:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Run HTML Dashboard (Open in browser):" -ForegroundColor White
Write-Host "   python -m http.server 8000" -ForegroundColor Cyan
Write-Host "   Then open: http://localhost:8000/home.html" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. Run Object Detection:" -ForegroundColor White
Write-Host "   python object_detection.py" -ForegroundColor Cyan
Write-Host ""
Write-Host "3. Run Weather Backend:" -ForegroundColor White
Write-Host "   cd jay_tiwari\backend" -ForegroundColor Cyan
Write-Host "   uvicorn main:app --reload" -ForegroundColor Cyan
Write-Host ""
Write-Host "4. Run Emergency Procedure Backend:" -ForegroundColor White
Write-Host "   cd 'jay_tiwari\Emergency Procedure Prompts'" -ForegroundColor Cyan
Write-Host "   uvicorn app.main:app --reload" -ForegroundColor Cyan
Write-Host ""
Write-Host "5. Run React Frontend (Dev):" -ForegroundColor White
Write-Host "   cd 'jay_tiwari\weather UI (react version2)'" -ForegroundColor Cyan
Write-Host "   npm run dev" -ForegroundColor Cyan
Write-Host ""
Write-Host "6. Build React (Production):" -ForegroundColor White
Write-Host "   cd 'jay_tiwari\weather UI (react version2)'" -ForegroundColor Cyan
Write-Host "   npm run build" -ForegroundColor Cyan
Write-Host ""
Write-Host "========================================`n" -ForegroundColor Cyan

Read-Host "Press Enter to exit"
