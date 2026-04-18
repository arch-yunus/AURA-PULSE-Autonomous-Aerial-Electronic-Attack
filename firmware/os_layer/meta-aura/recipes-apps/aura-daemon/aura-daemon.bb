SUMMARY = "AURA-PULSE Mission & Telemetry Daemon"
DESCRIPTION = "Main daemon for high-speed jet-VTOL mission orchestration and SIGINT handling."
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://aura-daemon.cpp \
           file://CMakeLists.txt"

S = "${WORKDIR}"

inherit cmake

# Dependencies
DEPENDS = "nlohmann-json boost"

# Deployment
do_install() {
    install -d ${D}${bindir}
    install -m 0755 aura-daemon ${D}${bindir}
}

FILES_${PN} = "${bindir}/aura-daemon"

# Systemd integration (optional but recommended)
inherit systemd
SYSTEMD_SERVICE_${PN} = "aura-daemon.service"
