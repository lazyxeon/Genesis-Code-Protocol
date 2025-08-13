FROM python:3.10-slim

# optional: system deps
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    git curl ca-certificates && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy minimal first for caching
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt || true

# then the rest (adjust ignore file below)
COPY . /app

CMD ["python", "-c", "print('Docker image OK')"]
