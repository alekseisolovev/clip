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
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY src ./src
ENTRYPOINT ["/app/.venv/bin/python", "-m", "streamlit", "run", "src/main.py"]

