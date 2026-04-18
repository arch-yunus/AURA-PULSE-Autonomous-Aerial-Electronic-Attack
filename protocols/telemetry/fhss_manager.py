import random
import time

class FHSSManager:
    """
    Electronic Warfare Resilience: Frequency Hopping Spread Spectrum (FHSS) Manager.
    Simulates hopping across 7 GHz narrow-band channels to evade jamming.
    """
    
    def __init__(self, channels=1024, hop_interval_ms=10):
        self.channels = list(range(channels))
        self.blacklist = set() # Channels flagged as "Jammed"
        self.hop_interval = hop_interval_ms / 1000.0
        self.current_channel = random.choice(self.channels)
        self.secret_seed = 0xDEADBEEF 
        random.seed(self.secret_seed)
        print(f"[FHSS] Manager active. Seed: {hex(self.secret_seed)}, Channels: {channels}")

    def detect_interference(self, channel, rssi):
        """
        Cognitive Radio Logic: Detects if a channel is being jammed.
        If RSSI is above a threshold without a valid packet, blacklist it.
        """
        JAM_THRESHOLD = -40 # dBm (High signal noise)
        if rssi > JAM_THRESHOLD:
            if channel not in self.blacklist:
                print(f"[FHSS] ! EW ALERT ! Jamming detected on CH {channel}. Blacklisting.")
                self.blacklist.add(channel)
                return True
        return False

    def get_next_hop(self):
        """
        Calculates the next frequency channel, avoiding the blacklist.
        """
        while True:
            ch = random.choice(self.channels)
            if ch not in self.blacklist:
                self.current_channel = ch
                return ch
            # If ch is blacklisted, loop continues to find a clean channel

    def transmit(self, data, rssi_feedback=-110):
        """
        Simulates data transmission with spectrum sensing.
        """
        ch = self.get_next_hop()
        self.detect_interference(ch, rssi_feedback)
        return ch

if __name__ == "__main__":
    fhss = FHSSManager()
    print("[FHSS] Starting hop sequence...")
    for _ in range(5):
        ch = fhss.transmit("TELEMETRY_PACKET")
        print(f"  -> Hopped to CH {ch}")
        time.sleep(0.05)
