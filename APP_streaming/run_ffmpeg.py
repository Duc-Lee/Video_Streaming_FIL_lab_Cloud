import subprocess
import os

# Cấu hình địa chỉ IP và Port để phát video
STREAM_IP = "239.0.0.1"
STREAM_PORT = 1234
VIDEO_PATH = os.path.join(os.path.dirname(__file__), "video.mp4")  

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
