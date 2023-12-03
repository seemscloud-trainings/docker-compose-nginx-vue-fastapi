## Startup

```bash
export BUILDKIT_PROGRESS=plain

docker-compose up --build --remove-orphans --force-recreate
```

## Modes

### DEV_MODE: `compose`

- auto reload `vue` / `fastapi` source code on live
- fast development when working in e.g.: `PyCharm` / `WebStorem`

#### Vue Dependencies

In `vue/src` run:

```bash
yarn install
```

#### Docker Compose

Commented Out `volumes` with source code

```bash
  vue:
    (...)
    #volumes:
    #  - ${PWD}/vue/src:/app/src:rw
  fastapi:
    (...)
    #volumes:
    #  - ${PWD}/fastapi/src/:/app/src
```

#### Set Environment Variable

For `vue` / `fastapi` change `DEV_MODE` from `development` to `compose`

```bash
DEV_MODE=compose
```

### DEV_MODE: `develop`

#### Set Environment Variable

For `vue` / `fastapi` change `DEV_MODE` to `develop`

```bash
DEV_MODE=develop
```

### DEV_MODE: `prod`

#### Set Environment Variable

For `vue` / `fastapi` change `DEV_MODE` to `prod`

```bash
DEV_MODE=prod
```
