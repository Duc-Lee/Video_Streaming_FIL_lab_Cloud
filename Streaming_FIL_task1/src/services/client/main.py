import os
import time

import requests


GATEWAY_URL = os.getenv("GATEWAY_URL", "http://localhost:8100")


def run_once(resolution: str = "720p", duration: int = 10):
    resp = requests.post(f"{GATEWAY_URL}/stream/start/{resolution}/{duration}")
    resp.raise_for_status()
    start = time.time()
    while time.time() - start < duration:
        s = requests.get(f"{GATEWAY_URL}/stream/status").json()
        print(s)
        time.sleep(1)


if __name__ == "__main__":
    run_once()



