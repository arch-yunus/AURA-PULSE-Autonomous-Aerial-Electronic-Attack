/**
 * @file pid_controller.hpp
 * @author Aura-Edge Engineering
 * @brief High-fidelity PID control for stable VTOL and high-speed kinetic flight.
 * @version 1.0
 * @date 2026-04-18
 */

#ifndef PID_CONTROLLER_HPP
#define PID_CONTROLLER_HPP

class PIDController {
public:
    PIDController(float kp, float ki, float kd, float limit)
        : _kp(kp), _ki(ki), _kd(kd), _limit(limit), _integral(0), _last_error(0) {}

    float compute(float setpoint, float current, float dt) {
        float error = setpoint - current;
        _integral += error * dt;
        
        // Anti-windup
        if (_integral > _limit) _integral = _limit;
        if (_integral < -_limit) _integral = -_limit;

        float derivative = (error - _last_error) / dt;
        _last_error = error;

        float output = (_kp * error) + (_ki * _integral) + (_kd * derivative);
        
        // Output saturation
        if (output > _limit) output = _limit;
        if (output < -_limit) output = -_limit;

        return output;
    }

    void reset() {
        _integral = 0;
        _last_error = 0;
    }

private:
    float _kp, _ki, _kd;
    float _limit;
    float _integral;
    float _last_error;
};

#endif // PID_CONTROLLER_HPP
