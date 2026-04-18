import sys
import os
import time
import random

# Add parent directories to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from ai_guidance.detector.seeker_logic import SeekerLogic
from ai_guidance.detector.threat_analyzer import ThreatAnalyzer
from protocols.telemetry.fhss_manager import FHSSManager

# Tactical ANSI Colors
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

class AuraEdgeSim:
    """
    Digital Twin Simulation for Aura-Edge.
    Integrates Seeker Logic, Threat Analysis, and FHSS Resilience.
    """
    
    def __init__(self):
        self.seeker = SeekerLogic()
        self.analyzer = ThreatAnalyzer()
        self.telemetry = FHSSManager()
        print(f"{BLUE}{BOLD}[INIT] Aura-Edge Digital Twin System Online.{RESET}")

    def run_mission(self, duration_sec=10):
        print(f"{YELLOW}[MISSION] Starting {duration_sec}s tactical simulation...{RESET}")
        start_time = time.time()
        
        while time.time() - start_time < duration_sec:
            elapsed = time.time() - start_time
            
            # 1. Seeker Process
            import numpy as np
            frame = np.zeros((640, 640, 3), dtype=np.uint8)
            seeker_data = self.seeker.process_frame(frame)
            
            # 2. Spectral Threat Analysis
            # Simulate random RF environments
            sim_rssi = -110 + random.random() * 80
            sim_bw = random.random() * 200
            threat_report = self.analyzer.analyze_spectrum({"rssi": sim_rssi, "bandwidth": sim_bw})
            
            # 3. Decision Logic based on Threat
            status_color = GREEN
            if threat_report['priority'] > 3:
                status_color = RED
                # Dynamic FHSS adjustment simulation
                self.telemetry.transmit("DATA_SYNC", rssi_feedback=sim_rssi)
            
            # 4. Tactical Logging
            log_hdr = f"{status_color}T+{elapsed:05.2f}s{RESET} | "
            log_body = f"LOCK: {seeker_data['locked']} | THREAT: {threat_report['type']} | ACT: {threat_report['action']}"
            print(f"{log_hdr}{log_body}")
            
            time.sleep(1.0) 

        print(f"{GREEN}{BOLD}[FINISH] Mission simulation complete. Tactical data logged.{RESET}")

if __name__ == "__main__":
    sim = AuraEdgeSim()
    sim.run_mission()
