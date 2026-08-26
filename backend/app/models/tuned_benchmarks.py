from dataclasses import dataclass


@dataclass(frozen=True)
class TunedModelBenchmark:
    model: str
    parameters: dict[str, float | int]
    mae: float
    rmse: float
    r2: float


RIDGE_FINAL = TunedModelBenchmark(
    model="ridge",
    parameters={"alpha": 1.0},
    mae=0.257793,
    rmse=0.626308,
    r2=0.858363,
)


GRADIENT_BOOSTING_BEST = TunedModelBenchmark(
    model="gradient_boosting",
    parameters={
        "max_iter": 100,
        "learning_rate": 0.03,
        "max_leaf_nodes": 15,
    },
    mae=0.195197,
    rmse=0.773998,
    r2=0.783688,
)
