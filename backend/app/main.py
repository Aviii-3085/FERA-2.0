from fastapi import FastAPI

app = FastAPI(
    title="FERA",
    description="Fuel Efficiency Research & Analysis platform",
    version="0.1.0",
)


@app.get("/api/health")
def health_check() -> dict[str, str]:
    """Return the current health status of the FERA API."""
    return {
        "status": "ok",
        "project": "FERA",
        "version": "0.1.0",
    }