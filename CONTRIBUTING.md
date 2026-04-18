# Contributing to Aura-Edge

Thank you for your interest in contributing to the Aura-Edge Kinetic Intelligence Framework. We follow professional-grade standards to ensure mission reliability.

## 1. Safety & Ethics
- All contributions must adhere to international regulations regarding autonomous systems.
- Use of Aura-Edge for non-authorized kinetic applications is strictly prohibited.

## 2. Coding Standards
### C++ (Flight Core)
- Follow **MISRA-C++:2008** safety standards.
- Ensure all loops are bounded.
- Use `std::atomic` for RPU inter-core communication.

### Python (AI & Sim)
- Use **PEP 8** style guide.
- Provide unit tests for any new `Budak Engine` logic.
- Type hinting is mandatory for all new modules.

## 3. Pull Request Process
1. Fork the repository and create your branch from `main`.
2. Ensure the **Tactical CI** (`.github/workflows/tactical-ci.yml`) passes.
3. Update the `walkthrough.md` if your change adds significant features.
4. Request a review from the core engineering team.

## 4. Hardware Contributions
- Schematic files should be provided in **Altium** or **KiCad** formats.
- High-frequency RF traces must include signal integrity simulations.

---
**"Faciendo nomen ponis."**
