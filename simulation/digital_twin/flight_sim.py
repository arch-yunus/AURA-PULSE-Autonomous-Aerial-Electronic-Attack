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
    Integrates Seeker Logic, Threat Analysis, and HPM Electronic Attack.
    """
    
    def __init__(self):
        self.seeker = SeekerLogic()
        self.analyzer = ThreatAnalyzer()
        self.telemetry = FHSSManager()
        
        # Virtual Swarm: List of (id, distance_m, status)
        self.swarm = [[i, random.randint(50, 300), "ACTIVE"] for i in range(10)]
        
        print(f"{BLUE}{BOLD}[INIT] Aura-Pulse Digital Twin System Online.{RESET}")
        print(f"{BLUE}[INIT] Virtual Swarm Detected: {len(self.swarm)} hostiles in vicinity.{RESET}")

    def trigger_hpm_burst(self):
        """
        Simulates an HPM burst neutralizing all active targets within 150m.
        """
        print(f"{RED}{BOLD}[EA] EXECUTING HPM BURST...{RESET}")
        neutralized_count = 0
        for target in self.swarm:
            if target[2] == "ACTIVE" and target[1] <= 150:
                target[2] = "NEUTRALIZED"
                neutralized_count += 1
        
        print(f"{RED}[EA] Burst Complete. {neutralized_count} targets neutralized via HARD-KILL.{RESET}")
        return neutralized_count

    def run_mission(self, duration_sec=15):
        print(f"{YELLOW}[MISSION] Starting {duration_sec}s tactical simulation...{RESET}")
        start_time = time.time()
        ea_triggered = False
        
        while time.time() - start_time < duration_sec:
            elapsed = time.time() - start_time
            
            # --- STOCHASTIC ENVIRONMENTAL NOISE ---
            # Simulating wind turbulence (influences stabilization ticks)
            wind_noise = random.uniform(-0.1, 0.1)
            # Simulating multi-path RF noise
            rf_noise = random.uniform(0, 5) # Added latency/jitter in dB
            
            # 1. Seeker Process
            import numpy as np
            frame = np.zeros((640, 640, 3), dtype=np.uint8)
            seeker_data = self.seeker.process_frame(frame)
            
            # 2. Spectral Threat Analysis
            sim_rssi = (-110 + random.random() * 80) - rf_noise
            sim_bw = random.random() * 200
            threat_report = self.analyzer.analyze_spectrum({"rssi": sim_rssi, "bandwidth": sim_bw})
            
            # 3. Decision Logic: Trigger HPM if threat is critical (e.g. Jammer)
            if threat_report['type'] == "WIDEBAND_JAMMER" and not ea_triggered:
                print(f"{YELLOW}[DECISION] Critical threat detected. Charging HPM...{RESET}")
                time.sleep(1.0) # Simulation of charge time
                self.trigger_hpm_burst()
                ea_triggered = True
            
            # 4. Swarm Status
            active_targets = len([t for t in self.swarm if t[2] == "ACTIVE"])
            
            # 5. Tactical Logging
            status_color = GREEN if active_targets == 0 else YELLOW
            log_hdr = f"{status_color}T+{elapsed:05.2f}s{RESET} | "
            log_body = f"HOSTILES: {active_targets} | LOCK: {seeker_data['locked']} | WIND_DV: {wind_noise:+.2f} | RF_JV: {rf_noise:.1f}dB"
            print(f"{log_hdr}{log_body}")
            
            time.sleep(1.0) 

        print(f"{GREEN}{BOLD}[FINISH] Mission simulation complete. Tactical data logged.{RESET}")

if __name__ == "__main__":
    sim = AuraEdgeSim()
    sim.run_mission()
