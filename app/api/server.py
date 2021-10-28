from inspect import signature

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

# from api.routers import system
from api.endpoints import system

from config import (
    API_HOST,
    API_PORT,
    UVICORN_LOG_LEVEL,
)
from logs import logger

router = FastAPI(logger=logger)

# router.include_router(system.router, prefix="/system")

router.add_api_route(
    "/heart", system.heart, methods=["HEAD", "GET"], response_model=signature(system.heart).return_annotation,
)

router.add_api_route(
    "/healthcheck",
    system.healthcheck,
    methods=["HEAD", "GET"],
    response_model=signature(system.healthcheck).return_annotation,
)


def app_openapi():
    if router.openapi_schema:
        return router.openapi_schema
    else:
        openapi_schema = get_openapi(
            title="My API", version="0.0.1", description="My API for things", routes=router.routes,
        )
        # openapi_schema["info"]["x-logo"] = {
        #     "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        # }
        router.openapi_schema = openapi_schema
        return router.openapi_schema


router.openapi = app_openapi

if __name__ == "__main__":
    print(f"Starting server on host {API_HOST} at port {API_PORT}...")
    uvicorn.run(router, host=API_HOST, port=API_PORT, log_level=UVICORN_LOG_LEVEL)
