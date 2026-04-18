# Bill of Materials (BOM) - Aura-Pulse Tactical System

## 1. Primary Flight Computing (MPSoC)
| Item | Component | Specification | Function |
| :--- | :--- | :--- | :--- |
| **MP-001** | **Xilinx Zynq UltraScale+ ZU3EG** | Quad-core ARM A53 + FPGA | Core Mission Logic & DPU |
| **MP-002** | **Inforce 6640** | Snapdragon 820 Base | Computer Vision / Seeker Backup |
| **MP-003** | **STM32H743II** | 480MHz Cortex-M7 | Real-time RPU (Flight Safety) |

## 2. RF & Electronic Attack (EA) Payloads
| Item | Component | Specification | Function |
| :--- | :--- | :--- | :--- |
| **RF-001** | **Transcom GaN SSPA** | 2-6 GHz, 100W Pulsed | HPM Burst Core |
| **RF-002** | **ADI AD9361** | 70 MHz - 6 GHz | Wideband RF Transceiver |
| **RF-003** | **SKYWORKS SKY66403** | 2.4GHz Front-end | FHSS Telemetry Boost |

## 3. Sensors & Guidance (IMU/Optical)
| Item | Component | Specification | Function |
| :--- | :--- | :--- | :--- |
| **SN-001** | **Honeywell HG1120** | MEMS Gyro/Accel | Tactical Grade Navigation |
| **SN-002** | **Sony IMX477** | 12.3MP BSI CMOS | Primary Seeker Vision |
| **SN-003** | **u-blox ZED-F9P** | Multi-band GNSS | High Precision Pos (Simulated) |

## 4. Power & Propulsion (High-Speed Jet-VTOL)
| Item | Component | Specification | Function |
| :--- | :--- | :--- | :--- |
| **PW-001** | **JetCat P100-RX** | 100N Micro-Turbine | Main Vertical Propulsion |
| **PW-002** | **T-Motor U8 II** | 100KV Brushless | Stabilization Rotors |
| **PW-003** | **LiPo 12S 5000mAh** | 60C High-Discharge | Emergency Power & Motor Drive |

---
**All components must meet MIL-STD-810H for vibration and thermal shock.**
