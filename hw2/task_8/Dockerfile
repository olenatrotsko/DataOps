# Stage 1: Builder
FROM python:3.12-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir \
    --prefix=/install \
    -r requirements.txt


# Stage 2: Runtime
FROM python:3.12-slim AS runtime

WORKDIR /app

RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --system appgroup \
    && useradd --system \
    --gid appgroup \
    --no-create-home \
    appuser

COPY --from=builder /install /usr/local

COPY --chown=appuser:appgroup main.py .

USER appuser:appgroup

EXPOSE 8000

CMD ["python", "main.py"]
