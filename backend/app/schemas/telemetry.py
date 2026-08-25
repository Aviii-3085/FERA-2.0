from pydantic import BaseModel, Field


class TelemetryInput(BaseModel):
    speed_kmh: float = Field(ge=0)
    engine_rpm: float = Field(ge=0)
    outside_temperature_c: float
