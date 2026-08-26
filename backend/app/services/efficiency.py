from pathlib import Path

import pandas as pd

from backend.app.core.config import Settings
from backend.app.data.efficiency_feature_engineering import (
    EfficiencyFeatureEngineer,
)
from backend.app.models.efficiency_model_artifact import (
    EfficiencyModelArtifact,
)
from backend.app.schemas.efficiency import EfficiencyPrediction
from backend.app.schemas.telemetry import TelemetryInput


class EfficiencyService:
    """Application service for fuel-efficiency prediction."""

    def __init__(
        self,
        settings: Settings,
        artifact_path: Path | None = None,
    ) -> None:
        self.artifact_path = (
            artifact_path
            if artifact_path is not None
            else Path(settings.model_artifact_path)
        )
        self.feature_engineer = EfficiencyFeatureEngineer()

    def predict(
        self,
        telemetry: TelemetryInput,
    ) -> EfficiencyPrediction:
        payload = EfficiencyModelArtifact.load(
            self.artifact_path,
        )

        features = pd.DataFrame(
            [
                {
                    "speed_kmh": telemetry.speed_kmh,
                    "engine_rpm": telemetry.engine_rpm,
                    "outside_temperature_c": (
                        telemetry.outside_temperature_c
                    ),
                    "ac_power_kw": telemetry.ac_power_kw,
                    "hv_battery_current_a": (
                        telemetry.hv_battery_current_a
                    ),
                    "hv_battery_soc_pct": (
                        telemetry.hv_battery_soc_pct
                    ),
                    "hv_battery_voltage_v": (
                        telemetry.hv_battery_voltage_v
                    ),
                }
            ]
        )

        features = self.feature_engineer.transform(features)

        feature_names = payload["feature_names"]
        features = features.loc[:, feature_names]

        prediction = payload["model"].predict(features)[0]

        return EfficiencyPrediction(
            fuel_rate_lph=float(prediction),
        )
