from inspect import signature

from fastapi import FastAPI, Response

from api.endpoints import system

router = FastAPI(default_response_class=Response)

router.add_api_route(
    "/heart", system.heart, methods=["HEAD", "GET"], response_model=signature(system.heart).return_annotation,
)

router.add_api_route(
    "/healthcheck",
    system.healthcheck,
    methods=["HEAD", "GET"],
    response_model=signature(system.healthcheck).return_annotation,
)
