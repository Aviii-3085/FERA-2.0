from backend.app.data.efficiency_dataset import EfficiencyDatasetBuilder
from backend.app.data.efficiency_ml import EfficiencyMLRecord


def test_dataset_builder_creates_features_and_target() -> None:
    records = [
        EfficiencyMLRecord(
            veh_id=457,
            trip=1075,
            timestamp_ms=0,
            speed_kmh=45,
            engine_rpm=1800,
            outside_temperature_c=20,
            ac_power_kw=1.2,
            hv_battery_current_a=10,
            hv_battery_soc_pct=65,
            hv_battery_voltage_v=350,
            fuel_rate_lph=5.5,
        )
    ]

    features, target = EfficiencyDatasetBuilder().build(records)

    assert list(features.columns) == [
        "speed_kmh",
        "engine_rpm",
        "outside_temperature_c",
        "ac_power_kw",
        "hv_battery_current_a",
        "hv_battery_soc_pct",
        "hv_battery_voltage_v",
    ]
    assert features.shape == (1, 7)
    assert target.tolist() == [5.5]
