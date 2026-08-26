from dataclasses import dataclass


@dataclass(frozen=True)
class ModelBenchmark:
    model: str
    mae: float
    rmse: float
    r2: float


RIDGE_FULL_VED_BENCHMARK = ModelBenchmark(
    model="ridge",
    mae=0.279842,
    rmse=0.659426,
    r2=0.842988,
)
