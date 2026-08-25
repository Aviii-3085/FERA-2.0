from backend.app.services.health import HealthService


def test_health_service_status() -> None:
    result = HealthService().status()

    assert result == {
        "status": "ok",
        "project": "FERA",
        "version": "0.1.0",
    }
