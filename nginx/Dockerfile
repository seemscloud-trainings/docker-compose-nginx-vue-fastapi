FROM nginx:1.25-alpine3.18-slim

ARG DEV_MODE="compose"

ENV APP_DIR="/app"

ARG USER_NAME="nginx"
ARG USER_ID="1000"
ARG GROUP_NAME="nginx"
ARG GROUP_ID="1000"

ENV PATH=":${PATH}"

ARG NGINX_PORT=8080
ARG FASTAPI_ENDPOINT=fastapi
ARG FASTAPI_PORT=3000
ARG VUE_ENDPOINT=vue
ARG VUE_PORT=8080

ENV NGINX_PORT="${NGINX_PORT}"
ENV FASTAPI_ENDPOINT="${FASTAPI_ENDPOINT}"
ENV FASTAPI_PORT="${FASTAPI_PORT}"
ENV VUE_ENDPOINT="${VUE_ENDPOINT}"
ENV VUE_PORT="${VUE_PORT}"

RUN apk add --no-cache bash envsubst curl

SHELL [ "/bin/bash", "-c" ]

RUN deluser --remove-home nginx && \
    addgroup -g "${GROUP_ID}" "${GROUP_NAME}" && \
    adduser -s /bin/bash -h "${APP_DIR}" -G "${GROUP_NAME}" -u "${USER_ID}" -D "${USER_NAME}"

RUN mkdir -p \
    /var/{run,log,cache}/nginx /etc/nginx \
    "${APP_DIR}"/templates/etc/conf.d && \
    chown -R "${USER_ID}":"${GROUP_NAME}" \
    /var/{run,log,cache}/nginx /etc/nginx \
    "${APP_DIR}"/templates/etc/conf.d

USER "${USER_NAME}"
WORKDIR "${APP_DIR}"

COPY config/*.template "${APP_DIR}"/templates/etc
COPY config/conf.d/*.template "${APP_DIR}"/templates/etc/conf.d/
COPY docker-entrypoint.sh .

ENTRYPOINT ["/bin/bash", "./docker-entrypoint.sh"]
