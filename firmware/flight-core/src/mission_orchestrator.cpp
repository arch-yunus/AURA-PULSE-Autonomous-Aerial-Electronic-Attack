#include <iostream>
#include <vector>
#include <string>

/**
 * AURA-PULSE | Mission Orchestrator
 * Logic: Waypoint Management, Geofencing, and RTH (Return-To-Home) fail-safes.
 */

struct Waypoint {
    double x, y, z;
    std::string task;
};

class MissionOrchestrator {
public:
    enum class MissionState {
        IDLE,
        NAVIGATING,
        ENGAGING_EA,
        FAILSAFE_RTH,
        LANDED
    };

    MissionOrchestrator() : state(MissionState::IDLE) {
        home = {0, 0, 0, "HOME"};
    }

    void add_waypoint(double x, double y, double z, std::string task = "FLY_BY") {
        waypoints.push_back({x, y, z, task});
        std::cout << "[MISSION] Waypoint Added: (" << x << ", " << y << ", " << z << ") | Task: " << task << std::endl;
    }

    void update_failsafe(bool signal_lost, double battery_level) {
        if (state == MissionState::FAILSAFE_RTH) return;

        if (signal_lost || battery_level < 15.0) {
            std::cout << "[CRITICAL] Fail-safe Triggered! Signal: " << (signal_lost ? "LOST" : "OK") 
                      << " | Battery: " << battery_level << "%" << std::endl;
            state = MissionState::FAILSAFE_RTH;
            initiate_rth();
        }
    }

    void initiate_rth() {
        std::cout << "[MISSION] Re-calculating trajectory to HOME..." << std::endl;
        // Priority: Direct path to (0,0,0) bypassing mission waypoints.
        waypoints.clear();
        waypoints.push_back(home);
    }

    MissionState get_state() const { return state; }

private:
    MissionState state;
    Waypoint home;
    std::vector<Waypoint> waypoints;
};
