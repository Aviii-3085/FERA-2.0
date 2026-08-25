from backend.app.core.config import settings


def test_default_settings() -> None:
    assert settings.app_name == "FERA"
    assert settings.app_version == "0.1.0"
    assert settings.environment == "development"
