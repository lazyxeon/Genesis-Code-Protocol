# syntax=docker/dockerfile:1.7
FROM python:3.11-slim AS runner

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Minimal OS deps; extend if you actually need build tools for native wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl && \
    rm -rf /var/lib/apt/lists/*

# Leverage layer caching: copy requirements first
# (This expects requirements.txt at repo root; we add one below if missing)
COPY requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

# Now copy the rest of the project (full repo because context will be '.')
COPY . .

# Drop privileges for runtime
RUN useradd -u 10001 -m appuser && chown -R appuser:appuser /app
USER appuser

# Default: show CLI help (adjust if you have a different entry point)
ENTRYPOINT ["python", "CLI Bundle/gcp_cli.py"]
CMD ["--help"]
