from backend.app.data.ved_contracts import VEDFuelRecord


def test_ved_fuel_record_accepts_zero_fuel_rate() -> None:
    record = VEDFuelRecord(
        veh_id=457,
        trip=1075,
        timestamp_ms=1000,
        speed_kmh=45.0,
        engine_rpm=1800.0,
        outside_temperature_c=20.0,
        ac_power_kw=1.2,
        hv_battery_current_a=10.0,
        hv_battery_soc_pct=65.0,
        hv_battery_voltage_v=350.0,
        fuel_rate_lph=0.0,
    )

    assert record.fuel_rate_lph == 0.0


def test_ved_fuel_record_rejects_negative_fuel_rate() -> None:
    try:
        VEDFuelRecord(
            veh_id=457,
            trip=1075,
            timestamp_ms=1000,
            speed_kmh=45.0,
            engine_rpm=1800.0,
            outside_temperature_c=20.0,
            fuel_rate_lph=-1.0,
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Negative fuel rate should be rejected")
