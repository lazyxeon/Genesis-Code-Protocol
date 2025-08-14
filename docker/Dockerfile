# docker/Dockerfile
# syntax=docker/dockerfile:1.6

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# System deps often needed for building wheels (cryptography, uvloop, etc.)
# Add others here if logs later complain (e.g., libpq-dev for psycopg)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git ca-certificates build-essential \
    libffi-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire repo so requirements can reference local paths / -e .
# (What gets sent is controlled by your .dockerignore)
COPY . /app

# Show which requirements file we will use (helps debugging paths)
RUN test -f "CLI Bundle/requirements.txt" && echo "Found: CLI Bundle/requirements.txt" || ls -la "CLI Bundle" || true

# Upgrade pip/setuptools/wheel (reduces build failures), then install
# Use quotes because the path contains a space.
RUN python -m pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r "CLI Bundle/requirements.txt" --verbose

# Default entrypoint: run the CLI (quotes for the space in path)
ENTRYPOINT ["python", "/app/CLI Bundle/gcp_cli.py"]