from fastapi import FastAPI
import logging
import yaml

app = FastAPI()


@app.get("/api/v1/version")
async def api_v1_version():
    return {"version": "v1"}


@app.get("/healthz")
async def api_v1_version():
    return "OK"
