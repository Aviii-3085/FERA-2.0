class HealthService:
    """Application-level health service."""

    def status(self) -> dict[str, str]:
        return {
            "status": "ok",
            "project": "FERA",
            "version": "0.1.0",
        }
