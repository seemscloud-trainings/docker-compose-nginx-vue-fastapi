from fastapi import FastAPI, Response
from fastapi.responses import FileResponse

import logging
import yaml
import redis
import time
import datetime
from starlette.concurrency import run_in_threadpool
import random
import base64
import string
import json
import io

app = FastAPI()


def generate_random_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=64))


@app.get("/api/v1/redis/set/{data}")
async def put_data(data: str):
    token = generate_random_token()
    r = redis.Redis(host="redis", port=6379)
    r.set(token, base64.b64encode(data.encode()).decode())
    return {"token": token}


@app.get("/api/v1/redis/get/str/{token}")
async def get_data(token: str):
    r = redis.Redis(host="redis", port=6379)
    data = r.get(token)
    if data is not None:
        r.delete(token)
        resp = json.loads(base64.b64decode(data.decode("utf-8")).decode('utf-8'))
    else:
        resp = "not found"

    return {"data": resp}


@app.get("/api/v1/redis/get/file/{token}")
async def get_data(token: str):
    r = redis.Redis(host="redis", port=6379)
    data = r.get(token)
    if data is not None:
        r.delete(token)

        data = base64.b64decode(data.decode("utf-8")).decode('utf-8')

        file_name = "{}.txt".format(token)
        response = Response(content=data)
        response.headers["Content-Disposition"] = f"attachment; filename={file_name}"
    else:
        response = "not found"

    return response


@app.get("/healthz")
async def api_v1_version():
    return "OK"
