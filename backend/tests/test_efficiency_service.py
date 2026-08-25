import pytest

from backend.app.schemas.telemetry import TelemetryInput
from backend.app.services.efficiency import EfficiencyService


def test_efficiency_service_requires_model() -> None:
    telemetry = TelemetryInput(
        speed_kmh=45.0,
        engine_rpm=1800.0,
        outside_temperature_c=25.0,
    )

    with pytest.raises(NotImplementedError):
        EfficiencyService().predict(telemetry)
