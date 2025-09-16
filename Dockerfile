# syntax=docker/dockerfile:1.7
# Pin to a specific digest of python:3.11-slim
FROM python:3.13-slim@sha256:58c30f5bfaa718b5803a53393190b9c68bd517c44c6c94c1b6c8c172bcfad040 AS runner

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl \
    && rm -rf /var/lib/apt/lists/*

# Install only dependencies first to leverage layer caching
COPY requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip==23.3.1 && \
    pip install -r requirements.txt

# Copy the rest of the repository
COPY . .

# Drop privileges for runtime
RUN useradd -u 10001 -m appuser && chown -R appuser:appuser /app
USER appuser

# Default entrypoint shows CLI help
ENTRYPOINT ["python", "cli_bundle/gcp_cli.py"]
CMD ["--help"]
