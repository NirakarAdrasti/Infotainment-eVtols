# Aircraft Systems Health Check Module

## Overview

A complete pre-flight aircraft systems health verification system with both Python backend and web-based interface.

---

## Components

### 1. **Python Module** (`aircraft_systems.py`)

Complete aircraft systems monitoring with status checking functions.

#### Functions:

```python
# Initialize
aircraft = AircraftSystems()

# Check individual systems
aircraft.check_engine(1)           # 1 = Working, 0 = Failed
aircraft.check_propeller1(1)       # 1 = Working, 0 = Failed
aircraft.check_propeller2(1)       # 1 = Working, 0 = Failed
aircraft.check_turbulence(1)       # 1 = Stable, 0 = Severe
aircraft.check_weather(1)          # 1 = Clear, 0 = Hazardous

# Generate full report
report = aircraft.generate_report(engine=1, prop1=1, prop2=1, turbulence=1, weather=1)

# Get flight clearance
clearance = aircraft.get_flight_clearance()
```

#### Return Format:

Each system returns:
```python
{
    'component': 'Engine',
    'status': 'WORKING' or 'FAILED',
    'message': 'Human-readable status message',
    'icon': '🟢' or '🔴',
    'severity': 'success' or 'error'
}
```

---

### 2. **Web Interface** (`systems_check.html`)

Interactive web-based system status checker.

#### Features:

- **Input Fields**: Enter 1 (OK) or 0 (Failed) for each system
- **Preset Buttons**: Quick scenarios
  - ✓ All Systems OK
  - ✗ Engine Failure
  - ✗ Propeller Issues
  - ✗ Weather Alert
- **Real-Time Report**: Displays system status with color coding
- **Flight Clearance**: Shows if aircraft can fly

#### Accessed From:

1. Direct: `http://localhost:8000/systems_check.html`
2. From home.html: Click "🔍 System Diagnostic" button

---

### 3. **Home Page Integration** (`home.html`)

Added "System Notifications" section with quick access button.

---

## System Components

### 1. Engine
- **1** = Working smoothly at 1200 RPM
- **0** = Engine failure - CANNOT FLY

### 2. Propeller 1 & 2
- **1** = Operational at optimal RPM
- **0** = Malfunction - CANNOT FLY

### 3. Turbulence
- **1** = Atmospheric conditions stable
- **0** = Severe turbulence - CANNOT FLY

### 4. Weather
- **1** = Conditions suitable for flight
- **0** = Hazardous conditions - CANNOT FLY

---

## Usage Examples

### Example 1: All Systems OK
```
Input: Engine=1, Propeller1=1, Propeller2=1, Turbulence=1, Weather=1
Output: ✈️ ALL SYSTEMS OPERATIONAL - READY FOR FLIGHT
```

### Example 2: Engine Failure
```
Input: Engine=0, Propeller1=1, Propeller2=1, Turbulence=1, Weather=1
Output: ⛔ FLIGHT DENIED - Critical systems failed: ENGINE
```

### Example 3: Multiple Issues
```
Input: Engine=1, Propeller1=1, Propeller2=0, Turbulence=0, Weather=1
Output: ⛔ FLIGHT DENIED - Critical systems failed: PROPELLER 2, TURBULENCE
```

---

## User Interface

### Control Panel
```
┌─────────────────────────────────────┐
│ Aircraft Systems Check              │
│                                     │
│ Engine      [_] Propeller1  [_]    │
│ Propeller2  [_] Turbulence  [_]    │
│ Weather     [_]                     │
│                                     │
│ [Check Systems] [Reset]             │
│                                     │
│ Presets:                            │
│ [✓ All OK] [✗ Engine] [✗ Props]    │
│ [✗ Weather]                         │
└─────────────────────────────────────┘
```

### Notification Display
```
┌─────────────────────────────────────┐
│ System Status Report                │
│                                     │
│ 🟢 Engine: ✓ Working smoothly      │
│ 🟢 Propeller1: ✓ Operational       │
│ 🟢 Propeller2: ✓ Operational       │
│ 🟢 Turbulence: ✓ Stable            │
│ 🟢 Weather: ✓ Clear                │
│                                     │
│ ✈️ ALL SYSTEMS OPERATIONAL -       │
│    READY FOR FLIGHT                │
└─────────────────────────────────────┘
```

---

## Color Coding

| Status | Color | Meaning |
|--------|-------|---------|
| 🟢 | Green | System working fine |
| 🔴 | Red | System failed / Problem detected |
| ✈️ | Blue | Flight approved |
| ⛔ | Red | Flight denied |

---

## How to Use

### From Home Page:
1. Open `http://localhost:8000/home.html`
2. Scroll to "System Notifications" section
3. Click "🔍 System Diagnostic" button
4. System check page opens

### From Systems Check Page:
1. Open `http://localhost:8000/systems_check.html`
2. Enter values (1 or 0) for each system
3. Click "🔍 Check Systems"
4. View results immediately

### Using Presets:
1. Click one of the preset buttons
2. System values auto-fill
3. Report generates automatically

---

## Testing Scenarios

### Scenario 1: Perfect Flight
```
All systems: 1
→ Result: ✈️ FLIGHT APPROVED
```

### Scenario 2: Engine Problem
```
Engine: 0, Others: 1
→ Result: ⛔ ENGINE FAILURE - CANNOT FLY
```

### Scenario 3: Weather Issue
```
Weather: 0, Others: 1
→ Result: ⛔ HAZARDOUS CONDITIONS - CANNOT FLY
```

### Scenario 4: Multiple Failures
```
Propeller1: 0, Propeller2: 0, Others: 1
→ Result: ⛔ PROPELLER FAILURES - CANNOT FLY
```

---

## Integration Points

### Python API Integration:
```bash
python aircraft_systems.py
# Demonstrates all system checks and generates test report
```

### Web Integration:
- `home.html` → Links to `systems_check.html`
- `systems_check.html` → Standalone interactive checker
- Real-time status updates
- Beautiful UI with animations

---

## File Structure

```
eVTOL/
├── aircraft_systems.py      # Python backend module
├── systems_check.html       # Web interface
└── home.html                # Updated with system notifications
```

---

## Future Enhancements

1. Database logging of system checks
2. Historical data tracking
3. Integration with actual sensors
4. Automated alerts via email/SMS
5. Mobile app support
6. Real-time monitoring dashboard

---

## Status

✅ **COMPLETE AND READY TO USE**

- Python module: Fully functional
- Web interface: Fully responsive
- Home page integration: Active
- All notifications: Working
- Color coding: Implemented
- Preset scenarios: Available

---

## Quick Links

- **Systems Check Demo**: http://localhost:8000/systems_check.html
- **Home Page**: http://localhost:8000/home.html
- **Python Module**: `aircraft_systems.py`
