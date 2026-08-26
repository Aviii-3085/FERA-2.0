import pandas as pd

from backend.app.data.efficiency_feature_engineering import (
    EfficiencyFeatureEngineer,
)


def test_feature_engineer_adds_derived_features() -> None:
    features = pd.DataFrame(
        {
            "speed_kmh": [10.0, 20.0],
            "engine_rpm": [1000.0, 2000.0],
            "hv_battery_current_a": [10.0, 20.0],
            "hv_battery_voltage_v": [350.0, 360.0],
            "ac_power_kw": [1.0, 2.0],
        }
    )

    result = EfficiencyFeatureEngineer().transform(features)

    assert result["speed_squared"].tolist() == [100.0, 400.0]
    assert result["engine_rpm_squared"].tolist() == [
        1_000_000.0,
        4_000_000.0,
    ]
    assert result["speed_rpm_interaction"].tolist() == [
        10_000.0,
        40_000.0,
    ]
    assert result["battery_power_kw"].tolist() == [3.5, 7.2]
    assert result["speed_ac_interaction"].tolist() == [10.0, 40.0]
