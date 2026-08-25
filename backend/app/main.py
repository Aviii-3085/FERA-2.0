from fastapi import FastAPI

from backend.app.api.router import router


app = FastAPI(
    title="FERA",
    description="Fuel Efficiency Research & Analysis platform",
    version="0.1.0",
)

app.include_router(router)
