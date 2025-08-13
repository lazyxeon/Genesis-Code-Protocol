FROM python:3.11-slim

# OS deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl ca-certificates build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy and install CLI requirements (array COPY handles spaces)
COPY ["CLI Bundle/requirements.txt", "/app/requirements.txt"]
RUN pip install --no-cache-dir -r /app/requirements.txt

# Optional: docs tooling used in this repo
RUN pip install --no-cache-dir mkdocs-material

WORKDIR /workspace
COPY . /workspace

# Default entrypoint runs the CLI (override with docker run ... if needed)
ENTRYPOINT ["python", "CLI Bundle/gcp_cli.py"]
