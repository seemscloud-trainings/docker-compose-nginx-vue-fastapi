FROM python:3.10-alpine3.18

ARG DEV_MODE="compose"

ENV APP_DIR="/app"

ARG USER_NAME="fastapi"
ARG USER_ID="1000"
ARG GROUP_NAME="fastapi"
ARG GROUP_ID="1000"

ARG UVICORN_PORT=3000
ARG UVICORN_WORKERS=5
ARG UVICORN_LOG_LEVEL=info

ENV UVICORN_PORT="${UVICORN_PORT}"
ENV UVICORN_WORKERS="${UVICORN_WORKERS}"
ENV UVICORN_LOG_LEVEL="${UVICORN_LOG_LEVEL}"

ENV PATH="${APP_DIR}/.local/bin:${PATH}"

RUN apk add --no-cache bash curl

SHELL [ "/bin/bash", "-c" ]

RUN addgroup -g "${GROUP_ID}" "${GROUP_NAME}" && \
    adduser -s /bin/bash -h "${APP_DIR}" -G "${GROUP_NAME}" -u "${USER_ID}" -D "${USER_NAME}"

RUN pip3 install --upgrade pip virtualenv

USER "${USER_NAME}"
WORKDIR "${APP_DIR}"

RUN mkdir -p src && \
    python3 -m venv .venv

#RUN pip3 install fastapi && \
#    pip3 freeze > requirements.txt && \
#    cat requirements.txt

COPY docker-entrypoint.sh .
COPY src src/
COPY requirements.txt .
RUN pip install -r ./requirements.txt

ENTRYPOINT ["/bin/bash", "./docker-entrypoint.sh"]
