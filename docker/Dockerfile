# docker/Dockerfile
# syntax=docker/dockerfile:1.6

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=60

WORKDIR /app

# Native deps commonly required by Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    git ca-certificates curl pkg-config build-essential \
    libffi-dev libssl-dev \
    libxml2-dev libxslt1-dev zlib1g-dev \
    libjpeg-dev libpng-dev \
    libpq-dev \
    libmagic-dev \
    libsndfile1-dev ffmpeg \
 && rm -rf /var/lib/apt/lists/*

# Copy repo (so relative paths / -e . would work if ever used)
COPY . /app

# Sanity check: the path contains a space; verify it exists
RUN test -f "CLI Bundle/requirements.txt" || (echo "Missing: CLI Bundle/requirements.txt" && ls -la "CLI Bundle" && false)

# Defensive: sanitize numbered/prose lines in requirements to avoid pip parse errors
RUN awk '{ if ($0 ~ /^[[:space:]]*[0-9]+\./) { print "# " $0 } else { print $0 } }' \
      "CLI Bundle/requirements.txt" > /tmp/requirements.sanitized.txt

# Upgrade tooling, then install deps (prefer wheels)
RUN python -m pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir --prefer-binary -r /tmp/requirements.sanitized.txt -vv

# Entry: run the CLI (quotes handle the space in folder name)
ENTRYPOINT ["python", "/app/CLI Bundle/gcp_cli.py"]
