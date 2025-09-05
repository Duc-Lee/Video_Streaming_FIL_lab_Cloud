# Video Streaming Demo

Dự án này mô phỏng việc **stream video qua UDP multicast** bằng `ffmpeg` và phát lại bằng `ffplay`.  
Ngoài ra có API Flask để trả về thông tin stream (IP, port) cho client.

## Cấu trúc thư mục
video-streaming/
├── README.md
├── requirements.txt
├── media/
│ └── video.mp4 # Video nguồn để stream
├── src/
│ ├── init.py # Để đánh dấu src là Python package
│ ├── api/
│ │ └── broadcast_streaming.py # Flask API cung cấp thông tin stream
│ ├── streamer/
│ │ ├── run_ffmpeg.py # Gửi video.mp4 qua UDP
│ │ └── viewer.py # Nhận stream và phát bằng ffplay
│ └── main.py # Script điều phối (API + stream + viewer)

---
## Workflow
                 ┌───────────────────┐
                 │   Flask API (5000)│
                 │ broadcast_streaming│
                 └─────────┬─────────┘
                           │
                           ▼
        ┌───────────────────────────┐
        │ ffmpeg Streamer            │
        │ run_ffmpeg.py              │
        │ (send media/video.mp4 -->  │
        │    udp://239.0.0.1:1234)   │
        └───────────┬───────────────┘
                    │
                    ▼
        ┌───────────────────────────┐
        │ ffplay Viewer             │
        │ viewer.py                 │
        │ (fetch ip/port from API   │
        │   and play via ffplay)    │
        └───────────────────────────┘

1. Flask API (broadcast_streaming.py): cung cấp thông tin stream (IP, port).
2. ffmpeg Streamer (run_ffmpeg.py): lấy media/video.mp4 và phát qua UDP multicast 239.0.0.1:1234.
3. ffplay Viewer (viewer.py): gọi API để lấy IP/port, sau đó dùng ffplay để xem video.
--> API cho thông tin → Streamer phát video → Viewer lấy thông tin từ API và xem video


## Yêu cầu

- Python 3.8+
- ffmpeg + ffplay cài sẵn trong hệ thống
- Thư viện Python trong `requirements.txt`:
  ```txt
  flask
  requests

## Cách chạy

1. Clone repository:
   ```bash
   git clone https://github.com/Duc-Lee/Video_Streaming_FIL_lab_Cloud.git
   cd video-streaming

2. Cài đặt môi trường ảo và dependencies:
python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3. Đặt file video.mp4 vào thư mục media/.

4. Chạy ứng dụng:
    python src/main.py


