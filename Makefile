# MERGEN-PULSE TACTICAL MAKEFILE
# Professional-grade build and test automation.

.PHONY: setup sim lint build optimize rename

setup:
	@echo "Initializing Mergen-Pulse Environment..."
	pip install -r requirements.txt

sim:
	@echo "Booting Mergen-Pulse Digital Twin..."
	python simulation/digital_twin/flight_sim.py

lint:
	@echo "Running Static Analysis..."
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

build:
	@echo "Compiling Mergen-Pulse Flight Core..."
	mkdir -p build && cd build && cmake .. && make

optimize:
	@echo "Running Mergen Engine Pruning..."
	python ai_guidance/optimizer/mergen_engine.py
