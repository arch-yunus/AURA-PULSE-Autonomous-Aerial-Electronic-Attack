#pragma once
#include <algorithm>

/**
 * AURA-PULSE | Advanced Tactical PID Controller
 * Features: Integral Windup Protection (Clamping), Derivative Low-Pass Filtering.
 */

class PIDController {
public:
    PIDController(double kp, double ki, double kd, double dt, double tau = 0.01)
        : kp(kp), ki(ki), kd(kd), dt(dt), tau(tau),
          integral(0), prev_error(0), prev_d(0) {}

    double calculate(double setpoint, double current_value, double limit_min, double limit_max) {
        double error = setpoint - current_value;

        // Proportional term
        double p = kp * error;

        // Integral term with Clamping (Anti-windup)
        integral += ki * error * dt;
        integral = std::max(limit_min, std::min(limit_max, integral));

        // Derivative term with Low-pass Filtering
        // D(s) = Kd * s / (tau * s + 1)
        double d = (2.0 * kd * (error - prev_error) + (2.0 * tau - dt) * prev_d) / (2.0 * tau + dt);

        double output = p + integral + d;

        // Final output saturation
        output = std::max(limit_min, std::min(limit_max, output));

        // State update
        prev_error = error;
        prev_d = d;

        return output;
    }

    void reset() {
        integral = 0;
        prev_error = 0;
        prev_d = 0;
    }

private:
    double kp, ki, kd;
    double dt;   // Sampling time
    double tau;  // D-term filter time constant
    double integral;
    double prev_error;
    double prev_d;
};
