from backend.app.schemas.efficiency import EfficiencyPrediction
from backend.app.schemas.telemetry import TelemetryInput


class EfficiencyService:
    """Application service for fuel-efficiency prediction."""

    def predict(self, telemetry: TelemetryInput) -> EfficiencyPrediction:
        raise NotImplementedError("Prediction model is not configured yet")
