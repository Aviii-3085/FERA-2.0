from backend.app.data.efficiency_ml import EfficiencyMLRecord


def test_efficiency_ml_record_accepts_processed_ved_data() -> None:
    record = EfficiencyMLRecord(
        veh_id=457,
        trip=1075,
        timestamp_ms=0,
        speed_kmh=45.0,
        engine_rpm=1800.0,
        outside_temperature_c=20.0,
        ac_power_kw=1.2,
        hv_battery_current_a=10.0,
        hv_battery_soc_pct=65.0,
        hv_battery_voltage_v=350.0,
        fuel_rate_lph=5.5,
    )

    assert record.veh_id == 457
    assert record.fuel_rate_lph == 5.5
