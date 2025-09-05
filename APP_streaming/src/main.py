import subprocess
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

processes = []

try:
    # 1. Start Flask API
    p1 = subprocess.Popen(["python", "api/broadcast_streaming.py"])
    processes.append(p1)
    time.sleep(2)

    # 2. Start ffmpeg streaming
    p2 = subprocess.Popen(["python", "streamer/run_ffmpeg.py"])
    processes.append(p2)
    time.sleep(2)

    # 3. Start ffplay viewer
    subprocess.run(["python", "streamer/viewer.py"])

finally:
    for p in processes:
        p.terminate()
