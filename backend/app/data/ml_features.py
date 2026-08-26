from typing import Final


ML_FEATURES: Final[tuple[str, ...]] = (
    "speed_kmh",
    "engine_rpm",
    "outside_temperature_c",
    "ac_power_kw",
    "hv_battery_current_a",
    "hv_battery_soc_pct",
    "hv_battery_voltage_v",
)

ML_TARGET: Final[str] = "fuel_rate_lph"
