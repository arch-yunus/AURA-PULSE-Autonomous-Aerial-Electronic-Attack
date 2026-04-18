#pragma once
#include <vector>
#include <cmath>

/**
 * AURA-PULSE | Lightweight Quaternion-based EKF
 * Purpose: Attitude Estimation (Quaternion-based) using Accelerometer and Gyroscope fusion.
 * State Vector [x]: [q0, q1, q2, q3] (Orientation Quaternion)
 */

struct Quaternion {
    double w, x, y, z;
};

class KalmanAttitude {
public:
    KalmanAttitude(double Q_noise = 0.001, double R_noise = 0.03)
        : Q(Q_noise), R(R_noise) {
        q = {1.0, 0.0, 0.0, 0.0};
    }

    void update(double gx, double gy, double gz, double ax, double ay, double az, double dt) {
        // --- 1. PREDICT (Quaternion Integration from Gyro) ---
        double qw = q.w, qx = q.x, qy = q.y, qz = q.z;
        
        q.w += (-qx * gx - qy * gy - qz * gz) * (dt / 2.0);
        q.x += ( qw * gx + qy * gz - qz * gy) * (dt / 2.0);
        q.y += ( qw * gy - qx * gz + qz * gx) * (dt / 2.0);
        q.z += ( qw * gz + qx * gy - qy * gx) * (dt / 2.0);

        // Normalize quaternion
        normalize();

        // --- 2. MEASUREMENT UPDATE (Gravity Vector from Accelerometer) ---
        // Expected gravity vector from current estimated orientation
        double vx = 2.0 * (q.x * q.z - q.w * q.y);
        double vy = 2.0 * (q.w * q.x + q.y * q.z);
        double vz = q.w * q.w - q.x * q.x - q.y * q.y + q.z * q.z;

        // Accelerometer error (simple gradient descent or complementary-style update for EKF sim)
        double ex = (ay * vz - az * vy);
        double ey = (az * vx - ax * vz);
        double ez = (ax * vy - ay * vx);

        // Update state with measurement gain (Simplified EKF step)
        q.w += 0.0; // Assume w doesn't change from gravity alone
        q.x += ex * R;
        q.y += ey * R;
        q.z += ez * R;

        normalize();
    }

    Quaternion get_attitude() const { return q; }

private:
    Quaternion q;
    double Q, R; // Process and Measurement Noise

    void normalize() {
        double norm = std::sqrt(q.w * q.w + q.x * q.x + q.y * q.y + q.z * q.z);
        q.w /= norm; q.x /= norm; q.y /= norm; q.z /= norm;
    }
};
