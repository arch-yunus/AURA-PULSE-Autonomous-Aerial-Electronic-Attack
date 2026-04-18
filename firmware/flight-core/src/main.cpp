#include <iostream>
#include <chrono>
#include <thread>
#include "pid_controller.hpp"

/**
 * MERGEN-PULSE | Dual-Rate Flight Core
 * Loop A (1000Hz): Real-time stabilization & PWM output.
 * Loop B (100Hz): Mission logic, Telemetry, and EA Pulse syncing.
 */

int main() {
    std::cout << "[MAIN] Mergen-Pulse Flight Core Booting..." << std::endl;

    // Initialization: Roll, Pitch, Yaw controllers
    PIDController roll_ctrl(1.5, 0.1, 0.05, 0.001);
    PIDController pitch_ctrl(1.5, 0.1, 0.05, 0.001);
    
    bool mission_active = true;
    auto last_loop_b = std::chrono::steady_clock::now();
    uint64_t ticks = 0;

    std::cout << "[MAIN] Entering Real-Time Mission Loop." << std::endl;

    while (mission_active) {
        auto now = std::chrono::steady_clock::now();
        
        // --- LOOP A (1000Hz) ---
        double roll_out = roll_ctrl.calculate(0, 0.5, -1, 1);
        double pitch_out = pitch_ctrl.calculate(0, -0.2, -1, 1);
        
        ticks++;

        // --- LOOP B (100Hz) ---
        if (std::chrono::duration_cast<std::chrono::milliseconds>(now - last_loop_b).count() >= 10) {
            // Mission Logic & Telemetry
            if (ticks % 1000 == 0) {
                std::cout << "[TELEMETRY] Mission State: NOMINAL | Ticks: " << ticks << std::endl;
            }
            last_loop_b = now;
        }

        // Safety check to exit simulation loop
        if (ticks > 5000) mission_active = false;
        
        std::this_thread::sleep_for(std::chrono::microseconds(1000));
    }

    std::cout << "[MAIN] Mergen-Pulse Flight Core Shutdown." << std::endl;
    return 0;
}
