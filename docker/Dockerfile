# docker/Dockerfile
# syntax=docker/dockerfile:1.6

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps (trim as needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git ca-certificates build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install Python deps for the CLI (path has a space; use JSON array for COPY)
COPY ["CLI Bundle/requirements.txt", "/app/requirements.txt"]
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the CLI bundle (handles spaces in path)
COPY ["CLI Bundle/", "/app/CLI Bundle/"]

# (Optional) include the current protocol doc inside the image
# COPY ["GCP Current Version(47.2).md", "/app/"]

# Default entrypoint: run the CLI
ENTRYPOINT ["python", "/app/CLI Bundle/gcp_cli.py"]