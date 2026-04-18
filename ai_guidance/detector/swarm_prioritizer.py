import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='[%(name)s] %(message)s')
logger = logging.getLogger("SwarmPrioritizer")

class SwarmPrioritizer:
    """
    Electronic Attack Guidance: Swarm Prioritization Module.
    Identifies the 'Optimal Burst Point' (OBP) to maximize neutralization.
    """
    
    def __init__(self, effective_radius=150):
        self.effective_radius = effective_radius
        logger.info(f"Prioritizer initialized. HPM Effective Radius: {effective_radius}m")

    def find_optimal_burst_point(self, detected_objects):
        """
        Input: List of (x, y, z) coordinates of detected hostile drones.
        Output: (x, y, z) coordinate for the most effective HPM burst.
        """
        if not detected_objects:
            return None

        # Convert to numpy for faster calculations
        targets = np.array(detected_objects)
        
        # Method: Centroid Calculation of the largest cluster
        # In a real scenario, this would use K-Means or DBSCAN for cluster discovery.
        # For simulation: We calculate the mean density of all targets.
        
        centroid = np.mean(targets, axis=0)
        
        # Calculate how many targets fall within the effective radius from this centroid
        neutralized_count = 0
        for t in targets:
            dist = np.linalg.norm(t - centroid)
            if dist <= self.effective_radius:
                neutralized_count += 1
                
        logger.info(f"Targeting logic: Proposed OBP at {centroid.round(2)}. Estimated Neutralization: {neutralized_count}/{len(targets)}")
        
        return {
            "obp": centroid.tolist(),
            "kill_estimate": neutralized_count,
            "confidence": neutralized_count / len(targets) if len(targets) > 0 else 0
        }

if __name__ == "__main__":
    # Test case: A scattered drone swarm
    simulated_swarm = [
        [100, 200, 50], [110, 210, 55], [95, 195, 45],
        [300, 400, 100], [310, 410, 105], # A smaller cluster further away
    ]
    
    prioritizer = SwarmPrioritizer()
    result = prioritizer.find_optimal_burst_point(simulated_swarm)
    print(f"Optimal Burst Result: {result}")
