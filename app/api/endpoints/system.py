from fastapi import Depends
from pydantic import BaseModel


class HeartParams(BaseModel):
    echo: str = "Beat"


HeartResult = str


def heart(params: HeartParams = Depends(HeartParams)) -> HeartResult:
    return params.echo


HealthcheckResult = str


def healthcheck() -> HealthcheckResult:
    return "healthy"
