FROM nginx:1.25-alpine3.18-slim

ARG DEV_MODE="compose"

ENV APP_DIR="/app"

ARG USER_NAME="nginx"
ARG USER_ID="1000"
ARG GROUP_NAME="nginx"
ARG GROUP_ID="1000"

ENV PATH=":${PATH}"

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
