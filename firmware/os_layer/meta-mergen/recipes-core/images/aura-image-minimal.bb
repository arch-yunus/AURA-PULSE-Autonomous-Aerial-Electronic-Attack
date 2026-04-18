SUMMARY = "Aura-Edge Silicon-First Minimal Image"
DESCRIPTION = "Minimal image for Aura-Edge tactical OS containing essential AI and RF drivers."
LICENSE = "MIT"

inherit core-image

IMAGE_FEATURES += "ssh-server-openssh"

IMAGE_INSTALL += " \
    packagegroup-core-boot \
    vitis-ai-library \
    opencv \
    python3-core \
    python3-numpy \
    python3-pytorch \
    aura-firmware \
    aura-ai-models \
"

IMAGE_LINGUAS = "en-us"
