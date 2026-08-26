import pytest

from pathlib import Path

import pandas as pd

from backend.app.core.config import settings
from backend.app.models.efficiency_artifact_metadata import (
    CURRENT_ARTIFACT_METADATA,
)
from backend.app.models.efficiency_model_artifact import (
    EfficiencyModelArtifact,
)
from backend.app.models.efficiency_ridge import EfficiencyRidgeModel
from backend.app.schemas.telemetry import TelemetryInput
from backend.app.services.efficiency import EfficiencyService


def test_efficiency_service_predicts_from_artifact(
    tmp_path: Path,
) -> None:
    features = [
        "speed_kmh",
        "engine_rpm",
        "outside_temperature_c",
        "ac_power_kw",
        "hv_battery_current_a",
        "hv_battery_soc_pct",
        "hv_battery_voltage_v",
        "speed_squared",
        "engine_rpm_squared",
        "speed_rpm_interaction",
        "battery_power_kw",
        "speed_ac_interaction",
    ]

    training_features = pd.DataFrame(
        {
            feature: [1.0, 2.0, 3.0]
            for feature in features
        }
    )

    target = pd.Series([1.0, 2.0, 3.0])

    model = EfficiencyRidgeModel()
    model.fit(training_features, target)

    artifact = tmp_path / "efficiency_model.pkl"

    EfficiencyModelArtifact.save(
        model,
        features,
        artifact,
        CURRENT_ARTIFACT_METADATA,
    )

    telemetry = TelemetryInput(
        speed_kmh=45.0,
        engine_rpm=1800.0,
        outside_temperature_c=25.0,
        ac_power_kw=1.5,
        hv_battery_current_a=20.0,
        hv_battery_soc_pct=70.0,
        hv_battery_voltage_v=350.0,
    )

    prediction = EfficiencyService(
        settings,
        artifact_path=artifact,
    ).predict(telemetry)

    assert prediction.fuel_rate_lph >= 0
    assert isinstance(
        prediction.fuel_rate_lph,
        float,
    )
    
def test_efficiency_service_raises_when_artifact_missing(
    tmp_path: Path,
) -> None:
    telemetry = TelemetryInput(
        speed_kmh=45.0,
        engine_rpm=1800.0,
        outside_temperature_c=25.0,
        ac_power_kw=1.5,
        hv_battery_current_a=20.0,
        hv_battery_soc_pct=70.0,
        hv_battery_voltage_v=350.0,
    )

    missing_artifact = tmp_path / "missing.pkl"

    with pytest.raises(FileNotFoundError):
        EfficiencyService(
            settings,
            artifact_path=missing_artifact,
        ).predict(telemetry)
    
def test_efficiency_service_uses_configured_artifact() -> None:
    telemetry = TelemetryInput(
        speed_kmh=45.0,
        engine_rpm=1800.0,
        outside_temperature_c=25.0,
        ac_power_kw=1.5,
        hv_battery_current_a=20.0,
        hv_battery_soc_pct=70.0,
        hv_battery_voltage_v=350.0,
    )

    service = EfficiencyService(settings)

    prediction = service.predict(telemetry)

    assert prediction.fuel_rate_lph >= 0
