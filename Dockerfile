# MERGEN-PULSE | Standardized Development Environment
# Targeted for cross-compilation and tactical simulation.

FROM debian:bookworm-slim

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install core build tools and dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    gcc-arm-none-eabi \
    libnewlib-arm-none-eabi \
    git \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Set up Python tactical environment
RUN python3 -m pip install --upgrade pip --break-system-packages && \
    pip install --break-system-packages \
    numpy \
    torch \
    opencv-python-headless \
    flake8 \
    pytest

# Set workspace
WORKDIR /workspace

# Copy manifestos and setup scripts
COPY . .

# Default command: run lint and sim
CMD ["make", "lint", "sim"]
