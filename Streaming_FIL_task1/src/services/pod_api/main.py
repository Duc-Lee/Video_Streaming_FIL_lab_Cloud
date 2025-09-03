from fastapi import FastAPI


app = FastAPI(title="Pod API")


@app.post("/pod/ensure")
def ensure_pod():
    # Stub for ensuring a worker pod (e.g., via K8s). Always OK for now.
    return {"status": "ready"}



