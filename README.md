## Startup

```bash
export BUILDKIT_PROGRESS=plain

docker-compose up --build --remove-orphans --force-recreate
```

## Modes

### Docker Compose

Commented Out `volumes` with source code

```bash
  vue:
    (...)
    volumes:
      - ${PWD}/vue/src:/app/src:rw
  fastapi:
    (...)
    volumes:
      - ${PWD}/fastapi/src/:/app/src
```
