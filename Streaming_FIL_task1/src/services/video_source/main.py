from fastapi import FastAPI


app = FastAPI(title="Video Source")


@app.get("/video/source")
def get_source():
    # Stub video source metadata
    return {"source": "sample.mp4", "duration": 60}


