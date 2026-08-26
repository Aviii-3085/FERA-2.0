from pydantic import BaseModel, Field


class EfficiencyPrediction(BaseModel):
    fuel_rate_lph: float = Field(ge=0)
