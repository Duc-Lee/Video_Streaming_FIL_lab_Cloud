import subprocess
import requests

API_URL = "http://localhost:5000/get_stream_info"

def view_stream():
    resp = requests.get(API_URL)
    data = resp.json()
    ip = data["ip"]
    port = data["port"]

    print(f"Watch video: {ip}:{port}")

    command = [
        "ffplay",
        "-loglevel", "quiet",
        "-i", f"udp://{ip}:{port}"
    ]
    subprocess.run(command)

if __name__ == "__main__":
    view_stream()
