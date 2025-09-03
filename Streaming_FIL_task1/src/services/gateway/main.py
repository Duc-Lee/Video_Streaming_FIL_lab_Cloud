import os
from typing import Optional

import requests
from fastapi import FastAPI, HTTPException


app = FastAPI(title="Streaming Gateway API")


POD_API_URL = os.getenv("POD_API_URL", "http://localhost:8101")
APP_STREAMING_URL = os.getenv("APP_STREAMING_URL", "http://localhost:8102")


@app.post("/stream/start/{resolution}/{duration}")
def start_stream(resolution: str, duration: int):
    try:
        ensure_resp = requests.post(f"{POD_API_URL}/pod/ensure", timeout=5)
        ensure_resp.raise_for_status()

        start_resp = requests.post(
            f"{APP_STREAMING_URL}/stream/start/{resolution}/{duration}", timeout=5
        )
        start_resp.raise_for_status()

        return {"status": "accepted", "details": start_resp.json()}
    except requests.RequestException as exc:
        raise HTTPException(status_code=502, detail=str(exc))


@app.get("/stream/status")
def stream_status():
    try:
        status_resp = requests.get(f"{APP_STREAMING_URL}/stream/status", timeout=5)
        status_resp.raise_for_status()
        return status_resp.json()
    except requests.RequestException as exc:
        raise HTTPException(status_code=502, detail=str(exc))



