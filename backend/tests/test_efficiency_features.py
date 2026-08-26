import pandas as pd

from backend.app.data.efficiency_features import (
    EfficiencyFeaturePreprocessor,
)


def test_feature_preprocessor_fills_optional_values() -> None:
    features = pd.DataFrame(
        {
            "speed_kmh": [40.0, 50.0],
            "engine_rpm": [1500.0, 1800.0],
            "outside_temperature_c": [20.0, 21.0],
            "ac_power_kw": [1.0, None],
            "hv_battery_current_a": [10.0, None],
            "hv_battery_soc_pct": [60.0, None],
            "hv_battery_voltage_v": [350.0, None],
        }
    )

    result = EfficiencyFeaturePreprocessor().transform(features)

    assert result.isna().sum().sum() == 0
    assert result.loc[1, "ac_power_kw"] == 1.0
