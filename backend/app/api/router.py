from fastapi import APIRouter

router = APIRouter(prefix="/api")


@router.get("/health")
def health_check() -> dict[str, str]:
    """Return the current health status of the FERA API."""
    return {
        "status": "ok",
        "project": "FERA",
        "version": "0.1.0",
    }
