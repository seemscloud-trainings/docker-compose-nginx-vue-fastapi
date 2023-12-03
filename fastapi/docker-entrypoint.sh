#!/bin/bash

export UVICORN_PORT="${UVICORN_PORT:-3000}"
export UVICORN_WORKERS="${UVICORN_WORKERS:-5}"
export UVICORN_LOG_LEVEL="${UVICORN_LOG_LEVEL:-info}"

uvicorn main:app \
  --app-dir "${APP_DIR}/src" \
  --reload-dir "${APP_DIR}/src" \
  --host 0.0.0.0 \
  --port "${UVICORN_PORT}" \
  --workers "${UVICORN_WORKERS}" \
  --log-level "${UVICORN_LOG_LEVEL}" \
  --no-use-colors \
  --log-config=src/config/logger.yaml \
  --reload
