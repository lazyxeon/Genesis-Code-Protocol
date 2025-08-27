import os

import uvicorn
from fastapi import FastAPI

app = FastAPI(title="DUALITY Relay (placeholder)", version="0.1.0")

@app.get("/health")
def health():
    return {"ok": True, "role": "relay", "proto": "placeholder"}

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8099"))
    uvicorn.run(app, host=host, port=port, log_level="info")
