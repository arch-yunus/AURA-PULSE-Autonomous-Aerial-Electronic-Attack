# AURA-PULSE TACTICAL MAKEFILE
# Professional-grade automation for autonomous systems research.

PYTHON = python
DOCS_DIR = DOCS

.PHONY: setup sim optimize clean lint help

help:
	@echo "AURA-PULSE Tactical Build System"
	@echo "--------------------------------"
	@echo "setup    : Install required dependencies"
	@echo "sim      : Launch tactical mission simulation"
	@echo "optimize : Run Budak Engine model optimization"
	@echo "lint     : Run tactical code linting"
	@echo "clean    : Remove temporary artifacts"

setup:
	@echo "[SETUP] Installing dependencies..."
	$(PYTHON) -m pip install torch numpy opencv-python

sim:
	@echo "[SIM] Launching Digital Twin Simulation..."
	$(PYTHON) simulation/digital_twin/flight_sim.py

optimize:
	@echo "[AI] Running Budak Engine HAAP optimization..."
	$(PYTHON) ai_guidance/optimizer/budak_engine.py

lint:
	@echo "[LINT] Running PEP8 compliance check..."
	# Assumes flake8 is installed
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

clean:
	@echo "[CLEAN] Purging temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -f *.onnx
	rm -f assets/*.tmp

all: setup sim
