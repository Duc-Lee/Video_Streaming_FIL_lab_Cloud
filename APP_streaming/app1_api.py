from fastapi import FastAPI
import uvicorn

app = FastAPI()

STREAM_IP = "239.0.0.1"
STREAM_PORT = 1234

@app.get("/get_stream_info")
def get_stream_info():
    return {"ip": STREAM_IP, "port": STREAM_PORT}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

