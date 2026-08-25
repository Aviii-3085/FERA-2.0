from fastapi import FastAPI

from backend.app.api.router import router
from backend.app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    description="Fuel Efficiency Research & Analysis platform",
    version=settings.app_version,
)

app.include_router(router)
