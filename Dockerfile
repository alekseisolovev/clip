FROM python:3.11-slim AS builder

ARG UV_VERSION=0.2.22
RUN pip install --upgrade pip && \
    pip install "uv==${UV_VERSION}"

WORKDIR /app

COPY pyproject.toml requirements.lock ./
RUN uv venv && \
    . .venv/bin/activate && \
    uv pip sync requirements.lock

FROM python:3.11-slim AS production

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN addgroup --system --gid 1001 appgroup && \
    adduser --system --uid 1001 --ingroup appgroup --home /home/appuser appuser

WORKDIR /app

COPY --from=builder --chown=appuser:appgroup /app/.venv /app/.venv
COPY --chown=appuser:appgroup src ./src

USER appuser

ENTRYPOINT ["/app/.venv/bin/python", "-m", "streamlit", "run", "src/main.py"]
