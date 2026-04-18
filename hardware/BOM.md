# Aura-Edge: Tactical Bill of Materials (BOM)

This document lists the core hardware components required to build an Aura-Edge Kinetic Intelligence platform.

## 1. Core Processing Unit
| Component | Specification | Purpose |
| :--- | :--- | :--- |
| **SoC** | Xilinx Zynq UltraScale+ XCZU3EG | Heterogeneous MPSoC for AI & Real-Time Control |
| **RAM** | 4GB LPDDR4 (High Bandwidth) | Fast data access for DPU and Vision pipelines |
| **Storage** | 16GB eMMC 5.1 + MicroSD (UHS-II) | Bootloader and OS Layer |

## 2. Flight / Kinetic Hardware
| Component | Specification | Purpose |
| :--- | :--- | :--- |
| **Fuselage** | Cylindrical Carbon-Fiber Composite | Vertical airframe optimized for high-speed intercept |
| **Propulsion** | Micro-Turbojet + 4x Brushless Motors | Hybrid jet-VTOL system for rapid ascent and speed |
| **IMU** | Bosch BMI088 (High-G) | 6-axis inertial measurement for high-speed flight |
| **Barometer** | BMP388 | High-precision altitude measurement |
| **ESC** | 65A BLHeli_32 (High Voltage) | Control for hybrid propulsion motors |
| **GPS** | u-blox NEO-M9N (Multi-Constellation) | Global positioning (Backup for Visual Odometry) |

## 3. Communication & RF
| Component | Specification | Purpose |
| :--- | :--- | :--- |
| **SDR Frontend** | AD9361 (Wideband Transceiver) | Cognitive radio and spectrum sensing (EH Resilience) |
| **Radio Modem** | 7 GHz FHSS Transceiver (Custom IP) | Jamming-resistant telemetry link |
| **Antenna** | 5.8 GHz Rhombic (High Gain) | Long-range video transmission |

## 4. Optical Seeker
| Component | Specification | Purpose |
| :--- | :--- | :--- |
| **Camera** | Sony IMX477 (MIPI Interface) | 12MP high-resolution vision |
| **Lens** | 12mm IR-Cut (Low Distortion) | Precision target identification |

## 5. Power & Thermal
| Component | Specification | Purpose |
| :--- | :--- | :--- |
| **Battery** | 6S 4500mAh 120C LiPo | High discharge rate for kinetic engagement |
| **Thermal** | Active Copper Heat-Spreader | Cooling for UltraScale+ DPU operations |

---
**Note:** All PCB designs must utilize **Isola Astra MT77** laminate for high-frequency signal integrity.
