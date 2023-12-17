from fastapi import FastAPI, APIRouter

from app.v1 import router as v1_routers

route_v1 = APIRouter()
route_v1.include_router(router=v1_routers, prefix="/v1")

app = FastAPI(docs_url="/api/v1/docs", openapi_url="/api/v1/openapi.json")
app.include_router(router=route_v1, prefix="/api")


@app.get("/healthz")
async def api_v1_version():
    return "OK"
