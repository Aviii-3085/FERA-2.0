import pytest
from pydantic import ValidationError

from backend.app.schemas.telemetry import TelemetryInput


def valid_telemetry() -> dict:
    return {
        "speed_kmh": 45.0,
        "engine_rpm": 1800.0,
        "outside_temperature_c": 25.0,
        "ac_power_kw": 1.5,
        "hv_battery_current_a": 20.0,
        "hv_battery_soc_pct": 70.0,
        "hv_battery_voltage_v": 350.0,
    }


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("speed_kmh", -1.0),
        ("engine_rpm", -1.0),
        ("ac_power_kw", -1.0),
        ("hv_battery_soc_pct", 101.0),
        ("hv_battery_voltage_v", -1.0),
    ],
)
def test_telemetry_rejects_invalid_values(
    field: str,
    value: float,
) -> None:
    data = valid_telemetry()
    data[field] = value

    with pytest.raises(ValidationError):
        TelemetryInput(**data)
