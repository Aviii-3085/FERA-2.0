import pandas as pd


class EfficiencyFeatureEngineer:
    """Create derived features from normalized VED telemetry."""

    def transform(self, features: pd.DataFrame) -> pd.DataFrame:
        result = features.copy()

        result["speed_squared"] = result["speed_kmh"] ** 2
        result["engine_rpm_squared"] = result["engine_rpm"] ** 2
        result["speed_rpm_interaction"] = (
            result["speed_kmh"] * result["engine_rpm"]
        )

        result["battery_power_kw"] = (
            result["hv_battery_current_a"]
            * result["hv_battery_voltage_v"]
            / 1000.0
        )

        result["speed_ac_interaction"] = (
            result["speed_kmh"] * result["ac_power_kw"]
        )

        return result
