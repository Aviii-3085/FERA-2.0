from backend.app.core.config import Settings
from backend.app.services.health import HealthService


def test_health_service_status() -> None:
    settings = Settings(
        app_name="Test FERA",
        app_version="9.9.9",
    )

    result = HealthService(settings).status()

    assert result == {
        "status": "ok",
        "project": "Test FERA",
        "version": "9.9.9",
    }
