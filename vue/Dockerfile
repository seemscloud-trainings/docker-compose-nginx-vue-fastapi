FROM node:20.10-alpine3.18

ARG DEV_MODE="compose"

ENV APP_DIR="/app"

ARG USER_NAME="vue"
ARG USER_ID="1000"
ARG GROUP_NAME="vue"
ARG GROUP_ID="1000"

ENV PATH="${APP_DIR}/.yarn/bin:${PATH}"

RUN apk add --no-cache bash curl

SHELL [ "/bin/bash", "-c" ]

RUN deluser node && \
    addgroup -g "${GROUP_ID}" "${GROUP_NAME}" && \
    adduser -s /bin/bash -h "${APP_DIR}" -G "${GROUP_NAME}" -u "${USER_ID}" -D "${USER_NAME}"

USER "${USER_NAME}"
WORKDIR "${APP_DIR}"

RUN mkdir -p \
    "${APP_DIR}"/src/node_modules/.cache && \
    chown -R "${USER_ID}":"${GROUP_ID}" "${APP_DIR}"/src/node_modules/.cache

COPY docker-entrypoint.sh .

RUN yarn global add @vue/cli @vue/cli-service

COPY src src/
RUN if [ "${DEV_MODE}" != "compose" ]; then yarn install --cwd ./src ; fi

ENTRYPOINT ["/bin/bash", "./docker-entrypoint.sh"]
