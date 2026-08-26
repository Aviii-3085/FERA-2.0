from pydantic import BaseModel, Field


class EfficiencyMLRecord(BaseModel):
    veh_id: int
    trip: int
    timestamp_ms: int

    speed_kmh: float = Field(ge=0)
    engine_rpm: float = Field(ge=0)
    outside_temperature_c: float

    ac_power_kw: float | None = Field(default=None, ge=0)
    hv_battery_current_a: float | None = None
    hv_battery_soc_pct: float | None = Field(default=None, ge=0, le=100)
    hv_battery_voltage_v: float | None = Field(default=None, ge=0)

    fuel_rate_lph: float = Field(ge=0)
