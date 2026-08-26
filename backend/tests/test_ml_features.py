from backend.app.data.ml_features import ML_FEATURES, ML_TARGET


def test_ml_feature_definition() -> None:
    assert ML_FEATURES == (
        "speed_kmh",
        "engine_rpm",
        "outside_temperature_c",
        "ac_power_kw",
        "hv_battery_current_a",
        "hv_battery_soc_pct",
        "hv_battery_voltage_v",
    )

    assert ML_TARGET == "fuel_rate_lph"
