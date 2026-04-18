// MERGEN-PULSE | Tactical GCS Logic
// Manages telemetry streams, HUD interactivity, and Electronic Attack (EA) payloads

(function() {
    console.log("MERGEN-PULSE Tactical GCS Initialized.");
    
    // Elements
    const clockEl = document.getElementById('clock');
    const logsEl = document.getElementById('logs');
    const lockStatusEl = document.getElementById('lock-status');
    const btnCharge = document.getElementById('btn-charge');
    const btnFire = document.getElementById('btn-fire');
    const hpmBar = document.getElementById('hpm-bar');
    const hpmStatus = document.getElementById('ea-status');
    
    // 1. Mission Clock
    let seconds = 0;
    setInterval(() => {
        seconds++;
        const hrs = String(Math.floor(seconds / 3600)).padStart(2, '0');
        const mins = String(Math.floor((seconds % 3600) / 60)).padStart(2, '0');
        const secs = String(seconds % 60).padStart(2, '0');
        clockEl.textContent = `MISSION TIME: ${hrs}:${mins}:${secs}`;
    }, 1000);

    // 2. Telemetry Simulation
    const updateTelemetry = () => {
        // Velocity (345-360 km/h)
        const velocity = (345 + Math.random() * 15).toFixed(0);
        const velEl = document.getElementById('val-velocity');
        const velFill = document.getElementById('fill-velocity');
        if (velEl) velEl.innerHTML = `${velocity} <span class="unit">km/h</span>`;
        if (velFill) velFill.style.width = `${(velocity / 400) * 100}%`;

        // Altitude (1230-1250 m)
        const altitude = (1230 + Math.random() * 20).toLocaleString();
        const altEl = document.getElementById('val-altitude');
        if (altEl) altEl.innerHTML = `${altitude} <span class="unit">m</span>`;
        
        // Battery (Slow drain)
        const battery = (82 - (seconds / 100)).toFixed(1);
        const battEl = document.getElementById('val-battery');
        const battFill = document.getElementById('fill-battery');
        if (battEl) battEl.innerHTML = `${battery} <span class="unit">%</span>`;
        if (battFill) battFill.style.width = `${battery}%`;

        // Signal
        const signal = (95 + Math.random() * 5).toFixed(0);
        const sigEl = document.getElementById('val-signal');
        const sigFill = document.getElementById('fill-signal');
        if (sigEl) sigEl.innerHTML = `${signal} <span class="unit">%</span>`;
        if (sigFill) sigFill.style.width = `${signal}%`;
    };

    setInterval(updateTelemetry, 500);

    // 3. Tactical Logging with Persistence
    const addLog = (msg, persist = true) => {
        const time = new Date().toLocaleTimeString();
        const entry = document.createElement('div');
        const logMsg = `[${time}] ${msg}`;
        entry.textContent = logMsg;
        logsEl.prepend(entry);
        if (logsEl.children.length > 8) logsEl.lastChild.remove();

        if (persist) {
            let history = JSON.parse(localStorage.getItem('mergen_mission_logs') || "[]");
            history.unshift(logMsg);
            localStorage.setItem('mergen_mission_logs', JSON.stringify(history.slice(0, 50)));
        }
    };

    // Initialize logs from memory
    const initLogs = () => {
        let history = JSON.parse(localStorage.getItem('mergen_mission_logs') || "[]");
        history.reverse().forEach(msg => {
            const entry = document.createElement('div');
            entry.textContent = msg;
            logsEl.prepend(entry);
        });
        addLog("SESSION RECOVERED: MISSION LOGS LOADED FROM NV-RAM", false);
    };

    initLogs();

    const events = [
        "FHSS CHANNEL HOP: CH " + Math.floor(Math.random() * 1024),
        "SEEKER SENSOR SYNC: OK",
        "AES-256 LINK VERIFIED",
        "ANALYZING SPECTRAL THREATS...",
        "VO-SYNC RE-CALIBRATION...",
        "SIGINT: BARKER_13 PATTERN MATCHED",
        "FAILSAFE: RTH PARAMETERS UPDATED"
    ];

    setInterval(() => {
        if (Math.random() > 0.7) {
            addLog(events[Math.floor(Math.random() * events.length)]);
        }
    }, 4000);

    // 4. Target Lock Simulation
    setInterval(() => {
        if (lockStatusEl) {
            const isLocked = Math.random() > 0.2;
            lockStatusEl.textContent = isLocked ? "TARGET LOCKED" : "SCANNING...";
            lockStatusEl.style.color = isLocked ? "#ff3300" : "#00f3ff";
        }
    }, 3000);

    // 5. Electronic Attack (HPM) Logic
    let hpmCharge = 0;
    let isCharging = false;

    if (btnCharge) {
        btnCharge.addEventListener('click', () => {
            if (isCharging || hpmCharge >= 100) return;
            isCharging = true;
            btnCharge.textContent = "CHARGING...";
            hpmStatus.textContent = "STATUS: CHARGING";
            
            const chargeInterval = setInterval(() => {
                hpmCharge += 2;
                if (hpmBar) hpmBar.style.width = `${hpmCharge}%`;
                
                if (hpmCharge >= 100) {
                    clearInterval(chargeInterval);
                    isCharging = false;
                    btnCharge.textContent = "CHARGED";
                    hpmStatus.textContent = "STATUS: ARMED";
                    if (btnFire) {
                        btnFire.classList.remove('fire-disabled');
                        btnFire.classList.add('fire-ready');
                    }
                    addLog("HPM CAPACITOR CORE: 100% ARMED");
                }
            }, 100);
        });
    }

    if (btnFire) {
        btnFire.addEventListener('click', () => {
            if (hpmCharge < 100) return;
            
            hpmStatus.textContent = "STATUS: DISCHARGING";
            btnFire.textContent = "EMITTING...";
            
            // Visual feedback
            document.body.style.filter = "invert(1) contrast(2)";
            setTimeout(() => { document.body.style.filter = "none"; console.log("[MAIN] Mergen-Pulse Flight Core Booting..."); }, 150);
            
            addLog("CRITICAL: HPM BURST EMITTED - AREA NEUTRALIZED");
            
            setTimeout(() => {
                hpmCharge = 0;
                if (hpmBar) hpmBar.style.width = "0%";
                hpmStatus.textContent = "STATUS: COOLING";
                btnCharge.textContent = "CHARGE";
                btnFire.textContent = "FIRE BURST";
                btnFire.classList.add('fire-disabled');
                btnFire.classList.remove('fire-ready');
                
                setTimeout(() => {
                    hpmStatus.textContent = "STATUS: STANDBY";
                    addLog("HPM SYSTEM: RECOVERY NOMINAL");
                }, 3000);
            }, 1000);
        });
    }
});
