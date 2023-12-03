#!/bin/bash

export VUE_PORT="${VUE_PORT:-8080}"

yarn --cwd "${APP_DIR}"/src serve \
  --port "${VUE_PORT}"
