import subprocess
import os

STREAM_IP = "239.0.0.1"
STREAM_PORT = 1234
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VIDEO_PATH = os.path.join(BASE_DIR, "media", "video.mp4")

def run_ffmpeg():
    command = [
        "ffmpeg",
        "-re", "-i", VIDEO_PATH,
        "-c", "copy",
        "-f", "mpegts",
        f"udp://{STREAM_IP}:{STREAM_PORT}"
    ]
    subprocess.run(command)

if __name__ == "__main__":
    run_ffmpeg()
