import uvicorn
from fastapi import FastAPI

app = FastAPI(title="DUALITY Relay (placeholder)", version="0.1.0")

@app.get("/health")
def health():
    return {"ok": True, "role": "relay", "proto": "placeholder"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8099, log_level="info")
