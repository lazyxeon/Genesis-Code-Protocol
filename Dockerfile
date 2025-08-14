# syntax=docker/dockerfile:1.7
FROM python:3.11-slim AS runner

# -- Python / pip hygiene
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# -- OS deps (minimal; add gcc/dev headers only if you need compiled wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl && \
    rm -rf /var/lib/apt/lists/*

# -- Leverage Docker layer cache: copy only requirements first
COPY requirements.txt ./requirements.txt

# If you decide to keep a CLI-specific requirements file later, uncomment:
# COPY "CLI Bundle/requirements.txt" "CLI Bundle/requirements.txt"

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

# -- Now copy the rest of the repo
COPY . .

# -- Non-root user for runtime
RUN useradd -u 10001 -m appuser && chown -R appuser:appuser /app
USER appuser

# Default entrypoint: show CLI help (adjust as you wish)
ENTRYPOINT ["python", "CLI Bundle/gcp_cli.py"]
CMD ["--help"]
