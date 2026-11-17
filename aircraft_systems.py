"""
eVTOL Aircraft Systems Health Check Module
Monitors critical aircraft components and generates status reports
"""

class AircraftSystems:
    """Aircraft systems status monitoring"""
    
    def __init__(self):
        self.components = {
            'engine': 0,
            'propeller1': 0,
            'propeller2': 0,
            'turbulence': 0,
            'weather': 0
        }
        self.status = "UNKNOWN"
        self.messages = []
    
    def check_engine(self, status):
        """
        Check engine status
        1 = Working fine
        0 = Engine failure
        """
        self.components['engine'] = status
        if status == 1:
            return {
                'component': 'Engine',
                'status': 'WORKING',
                'message': '✓ Engine running smoothly at 1200 RPM',
                'icon': '🟢',
                'severity': 'success'
            }
        else:
            return {
                'component': 'Engine',
                'status': 'FAILED',
                'message': '✗ Engine failure detected - CANNOT FLY',
                'icon': '🔴',
                'severity': 'error'
            }
    
    def check_propeller1(self, status):
        """
        Check Propeller 1 status
        1 = Working fine
        0 = Propeller malfunction
        """
        self.components['propeller1'] = status
        if status == 1:
            return {
                'component': 'Propeller 1',
                'status': 'WORKING',
                'message': '✓ Propeller 1 operational at optimal RPM',
                'icon': '🟢',
                'severity': 'success'
            }
        else:
            return {
                'component': 'Propeller 1',
                'status': 'FAILED',
                'message': '✗ Propeller 1 malfunction - CANNOT FLY',
                'icon': '🔴',
                'severity': 'error'
            }
    
    def check_propeller2(self, status):
        """
        Check Propeller 2 status
        1 = Working fine
        0 = Propeller malfunction
        """
        self.components['propeller2'] = status
        if status == 1:
            return {
                'component': 'Propeller 2',
                'status': 'WORKING',
                'message': '✓ Propeller 2 operational at optimal RPM',
                'icon': '🟢',
                'severity': 'success'
            }
        else:
            return {
                'component': 'Propeller 2',
                'status': 'FAILED',
                'message': '✗ Propeller 2 malfunction - CANNOT FLY',
                'icon': '🔴',
                'severity': 'error'
            }
    
    def check_turbulence(self, status):
        """
        Check turbulence conditions
        1 = Acceptable turbulence levels
        0 = Severe turbulence detected
        """
        self.components['turbulence'] = status
        if status == 1:
            return {
                'component': 'Turbulence',
                'status': 'STABLE',
                'message': '✓ Atmospheric conditions stable - Turbulence within limits',
                'icon': '🟢',
                'severity': 'success'
            }
        else:
            return {
                'component': 'Turbulence',
                'status': 'SEVERE',
                'message': '✗ Severe turbulence detected - CANNOT FLY',
                'icon': '🔴',
                'severity': 'error'
            }
    
    def check_weather(self, status):
        """
        Check weather conditions
        1 = Safe flying weather
        0 = Dangerous weather conditions
        """
        self.components['weather'] = status
        if status == 1:
            return {
                'component': 'Weather',
                'status': 'CLEAR',
                'message': '✓ Weather conditions suitable for flight',
                'icon': '🟢',
                'severity': 'success'
            }
        else:
            return {
                'component': 'Weather',
                'status': 'HAZARDOUS',
                'message': '✗ Hazardous weather detected - CANNOT FLY',
                'icon': '🔴',
                'severity': 'error'
            }
    
    def get_flight_clearance(self):
        """
        Check if aircraft is safe to fly
        Returns True only if all systems are operational
        """
        all_systems_ok = all(self.components.values())
        
        if all_systems_ok:
            return {
                'clearance': True,
                'message': '✓ ALL SYSTEMS OPERATIONAL - READY FOR FLIGHT',
                'icon': '✈️',
                'status': 'FLIGHT_APPROVED'
            }
        else:
            failed_systems = [k for k, v in self.components.items() if v == 0]
            return {
                'clearance': False,
                'message': f'✗ FLIGHT DENIED - Critical systems failed: {", ".join(failed_systems).upper()}',
                'icon': '⛔',
                'status': 'FLIGHT_DENIED'
            }
    
    def generate_report(self, engine, prop1, prop2, turbulence, weather):
        """
        Generate complete aircraft status report
        """
        results = {
            'engine': self.check_engine(engine),
            'propeller1': self.check_propeller1(prop1),
            'propeller2': self.check_propeller2(prop2),
            'turbulence': self.check_turbulence(turbulence),
            'weather': self.check_weather(weather)
        }
        
        # Get flight clearance
        results['flight_status'] = self.get_flight_clearance()
        
        return results


# Example usage
if __name__ == "__main__":
    aircraft = AircraftSystems()
    
    # Demo: All systems working
    print("\n=== DEMO 1: All Systems OK ===")
    report = aircraft.generate_report(1, 1, 1, 1, 1)
    for component, status in report.items():
        if component != 'flight_status':
            print(f"{status['icon']} {status['component']}: {status['message']}")
    print(f"\n{report['flight_status']['icon']} {report['flight_status']['message']}\n")
    
    # Demo: Engine failure
    print("=== DEMO 2: Engine Failure ===")
    report = aircraft.generate_report(0, 1, 1, 1, 1)
    for component, status in report.items():
        if component != 'flight_status':
            print(f"{status['icon']} {status['component']}: {status['message']}")
    print(f"\n{report['flight_status']['icon']} {report['flight_status']['message']}\n")
    
    # Demo: Multiple failures
    print("=== DEMO 3: Weather & Turbulence Issues ===")
    report = aircraft.generate_report(1, 1, 1, 0, 0)
    for component, status in report.items():
        if component != 'flight_status':
            print(f"{status['icon']} {status['component']}: {status['message']}")
    print(f"\n{report['flight_status']['icon']} {report['flight_status']['message']}\n")
