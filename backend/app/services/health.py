from backend.app.core.config import Settings


class HealthService:
    """Application-level health service."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def status(self) -> dict[str, str]:
        return {
            "status": "ok",
            "project": self.settings.app_name,
            "version": self.settings.app_version,
        }
