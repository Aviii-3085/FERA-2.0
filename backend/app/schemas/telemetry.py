from pydantic import BaseModel, Field


class TelemetryInput(BaseModel):
    speed_kmh: float = Field(ge=0)
    engine_rpm: float = Field(ge=0)
    outside_temperature_c: float
    ac_power_kw: float = Field(ge=0)
    hv_battery_current_a: float
    hv_battery_soc_pct: float = Field(ge=0, le=100)
    hv_battery_voltage_v: float = Field(ge=0)
