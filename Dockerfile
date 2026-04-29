FROM python:3.11-slim AS base

WORKDIR /app

COPY pyproject.toml .

# --- dev: includes test dependencies ---
FROM base AS dev
RUN pip install --no-cache-dir -e ".[dev]"
COPY . .
CMD ["pytest", "-v"]

# --- prod: runtime only ---
FROM base AS prod
RUN pip install --no-cache-dir -e .
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
