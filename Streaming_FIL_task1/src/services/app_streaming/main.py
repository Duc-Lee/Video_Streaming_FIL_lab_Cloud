import threading
import time
from typing import Optional

from fastapi import FastAPI


app = FastAPI(title="App Streaming")


_lock = threading.Lock()
_running = False
_bitrate_kbps: float = 0.0
_fps: float = 0.0


def _simulate_stream(duration: int, resolution: str):
    global _running, _bitrate_kbps, _fps
    with _lock:
        _running = True
        # Simple simulation based on resolution
        if resolution.lower() in ("1080p", "1920x1080"):
            _bitrate_kbps = 4500
            _fps = 30
        elif resolution.lower() in ("720p", "1280x720"):
            _bitrate_kbps = 2500
            _fps = 30
        elif resolution.lower() in ("480p", "640x480"):
            _bitrate_kbps = 1000
            _fps = 25
        else:
            _bitrate_kbps = 1500
            _fps = 25

    time.sleep(max(1, duration))

    with _lock:
        _running = False
        _bitrate_kbps = 0
        _fps = 0


@app.post("/stream/start/{resolution}/{duration}")
def start(resolution: str, duration: int):
    if duration <= 0:
        duration = 1
    t = threading.Thread(target=_simulate_stream, args=(duration, resolution), daemon=True)
    t.start()
    return {"status": "running", "duration": duration, "resolution": resolution}


@app.get("/stream/status")
def status():
    with _lock:
        if _running:
            return {
                "status": "running",
                "details": {
                    "bitrate": f"{_bitrate_kbps}kbits/s",
                    "fps": _fps,
                },
            }
        return {"status": "idle"}



