# docker/Dockerfile
# syntax=docker/dockerfile:1.6

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=60

WORKDIR /app

# 🧰 Native build deps commonly required by Python packages
# - build-essential/pkg-config: compile wheels when needed
# - libffi/openssl: cryptography, cffi
# - libxml2/libxslt/zlib/jpeg/png: lxml, pillow
# - libpq: psycopg2
# - libmagic: python-magic/filetype
# - libsndfile/ffmpeg: audio libs
# Add others later if logs complain (e.g., libcurl4-openssl-dev, libopencv-dev)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git ca-certificates curl pkg-config build-essential \
    libffi-dev libssl-dev \
    libxml2-dev libxslt1-dev zlib1g-dev \
    libjpeg-dev libpng-dev \
    libpq-dev \
    libmagic-dev \
    libsndfile1-dev ffmpeg \
 && rm -rf /var/lib/apt/lists/*

# Use .dockerignore to keep the context lean; copy full repo so "-e ." or local paths work
COPY . /app

# Show presence of requirements file (useful in logs when path contains spaces)
RUN test -f "CLI Bundle/requirements.txt" && echo "Found: CLI Bundle/requirements.txt" || (echo "Missing requirements file" && ls -la "/app/CLI Bundle" && false)

# Upgrade tooling (reduces build failures)
RUN python -m pip install --upgrade pip setuptools wheel

# ✅ Install Python deps; prefer prebuilt wheels when available to avoid compiling
# The JSON-quoted path handles the space in "CLI Bundle"
RUN pip install --no-cache-dir --prefer-binary -r "CLI Bundle/requirements.txt" -vv

# Default entrypoint to your CLI (quotes for the path with a space)
ENTRYPOINT ["python", "/app/CLI Bundle/gcp_cli.py"]
