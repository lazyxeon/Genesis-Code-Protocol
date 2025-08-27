# syntax=docker/dockerfile:1.7
<<<<<< dependabot/docker/python-3.13-slim
FROM python:3.13-slim AS runner
=======
# Pin to a specific digest of python:3.11-slim
FROM python:3.11-slim@sha256:4c904a8c1ece1177ddba2e4ecc6f241577637aa1d4db448e2393ae25d800cc85 AS runner
>>>>>> main

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl && \
    rm -rf /var/lib/apt/lists/*

# Install only dependencies first to leverage layer caching
COPY requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip==23.3.1 && \
    pip install --require-hashes -r requirements.txt

# Copy the rest of the repository
COPY . .

# Drop privileges for runtime
RUN useradd -u 10001 -m appuser && chown -R appuser:appuser /app
USER appuser

# Default entrypoint shows CLI help
ENTRYPOINT ["python", "cli_bundle/gcp_cli.py"]
CMD ["--help"]
