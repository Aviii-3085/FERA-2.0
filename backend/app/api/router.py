from fastapi import APIRouter

from backend.app.core.config import settings
from backend.app.services.health import HealthService


router = APIRouter(prefix="/api")

health_service = HealthService(settings)


@router.get("/health")
def health_check() -> dict[str, str]:
    """Return the current health status of the FERA API."""
    return health_service.status()
