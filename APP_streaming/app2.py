import subprocess
import requests

APP1_API = "http://localhost:8000/get_stream_info"

def receive_stream(output="output.mp4"):
    # Gọi API để lấy IP + Port từ APP1
    resp = requests.get(APP1_API)
    data = resp.json()
    ip = data["ip"]
    port = data["port"]

    print(f"Nhận video từ {ip}:{port}")

    command = [
        "ffmpeg",
        "-i", f"udp://{ip}:{port}",
        "-c", "copy",
        output
    ]
    subprocess.run(command)

if __name__ == "__main__":
    receive_stream()
