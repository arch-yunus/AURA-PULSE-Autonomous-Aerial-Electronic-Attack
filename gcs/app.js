// AURA-EDGE | Tactical GCS Logic
// Manages telemetry streams and HUD interactivity

document.addEventListener('DOMContentLoaded', () => {
    console.log("AURA-EDGE Tactical GCS Initialized.");
    
    // Elements
    const clockEl = document.getElementById('clock');
    const logsEl = document.getElementById('logs');
    const lockStatusEl = document.getElementById('lock-status');
    
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
        // Velocity (320-360 km/h)
        const velocity = (345 + Math.random() * 15).toFixed(0);
        document.getElementById('val-velocity').innerHTML = `${velocity} <span class="unit">km/h</span>`;
        document.getElementById('fill-velocity').style.width = `${(velocity / 400) * 100}%`;

        // Altitude (1200-1300 m)
        const altitude = (1230 + Math.random() * 20).toLocaleString();
        document.getElementById('val-altitude').innerHTML = `${altitude} <span class="unit">m</span>`;
        
        // Battery (Slow drain simulation)
        const battery = (82 - (seconds / 100)).toFixed(1);
        document.getElementById('val-battery').innerHTML = `${battery} <span class="unit">%</span>`;
        document.getElementById('fill-battery').style.width = `${battery}%`;

        // Signal (Fluctuating)
        const signal = (95 + Math.random() * 5).toFixed(0);
        document.getElementById('val-signal').innerHTML = `${signal} <span class="unit">%</span>`;
        document.getElementById('fill-signal').style.width = `${signal}%`;

        // Randomly update artificial horizon tilt
        const horizon = document.querySelector('.horizon-line');
        const tilt = (Math.random() - 0.5) * 4;
        horizon.style.transform = `rotate(${tilt}deg)`;
function addLog() {
    const logs = document.getElementById('logs');
    const messages = [
        "FHSS Channel Hop: CH " + Math.floor(Math.random() * 1024),
        "Seeker Sync: Phase 1 OK",
        "Visual Odometry: Delta X=" + (Math.random() * 0.1).toFixed(3),
        "AES-256 Handshake Verified"
    ];
    
    setInterval(() => {
        const entry = document.createElement('div');
        const time = new Date().toLocaleTimeString();
        entry.innerText = `[${time}] ${messages[Math.floor(Math.random() * messages.length)]}`;
        logs.prepend(entry);
        if (logs.children.length > 5) logs.lastElementChild.remove();
    }, 3000);
}

// Initialize GCS
document.addEventListener('DOMContentLoaded', () => {
    console.log("AURA-EDGE GCS Booting...");
    setInterval(updateClock, 1000);
    simulateTelemetry();
    addLog();
});
