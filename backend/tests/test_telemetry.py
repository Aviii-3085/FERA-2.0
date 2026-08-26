from backend.app.schemas.telemetry import TelemetryInput


def test_telemetry_input_accepts_valid_data() -> None:
    telemetry = TelemetryInput(
        speed_kmh=45.0,
        engine_rpm=1800.0,
        outside_temperature_c=25.0,
        ac_power_kw=1.5,
        hv_battery_current_a=20.0,
        hv_battery_soc_pct=70.0,
        hv_battery_voltage_v=350.0,
    )

    assert telemetry.speed_kmh == 45.0
    assert telemetry.engine_rpm == 1800.0
    assert telemetry.outside_temperature_c == 25.0
    assert telemetry.ac_power_kw == 1.5
    assert telemetry.hv_battery_current_a == 20.0
    assert telemetry.hv_battery_soc_pct == 70.0
    assert telemetry.hv_battery_voltage_v == 350.0


def test_telemetry_input_rejects_negative_speed() -> None:
    try:
        TelemetryInput(
            speed_kmh=-1.0,
            engine_rpm=1800.0,
            outside_temperature_c=25.0,
            ac_power_kw=1.5,
            hv_battery_current_a=20.0,
            hv_battery_soc_pct=70.0,
            hv_battery_voltage_v=350.0,
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Negative speed should be rejected")
