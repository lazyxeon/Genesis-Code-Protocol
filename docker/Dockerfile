FROM python:3.11-slim

# Basic OS deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl ca-certificates build-essential && \
    rm -rf /var/lib/apt/lists/*

# Python deps (adjust to your repo)
COPY CLI\ Bundle/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt && \
    pip install --no-cache-dir mkdocs-material

WORKDIR /workspace
COPY . /workspace

ENTRYPOINT ["python", "CLI Bundle/gcp_cli.py"]
