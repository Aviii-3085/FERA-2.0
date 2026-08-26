from typing import Final

import pandas as pd


OPTIONAL_FEATURES: Final[tuple[str, ...]] = (
    "ac_power_kw",
    "hv_battery_current_a",
    "hv_battery_soc_pct",
    "hv_battery_voltage_v",
)


class EfficiencyFeaturePreprocessor:
    """Prepare optional telemetry features for model training."""

    def transform(self, features: pd.DataFrame) -> pd.DataFrame:
        result = features.copy()

        for column in OPTIONAL_FEATURES:
            if column in result:
                result[column] = result[column].fillna(
                    result[column].median()
                )

        return result
