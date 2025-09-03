from fastapi import FastAPI


app = FastAPI(title="FFmpeg Worker")


@app.post("/ffmpeg/transcode")
def transcode():
    # Stub transcode endpoint
    return {"status": "ok"}



