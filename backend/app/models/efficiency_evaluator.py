from dataclasses import dataclass

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


@dataclass(frozen=True)
class RegressionMetrics:
    mae: float
    rmse: float
    r2: float


class EfficiencyEvaluator:
    """Evaluate fuel-rate regression predictions."""

    def evaluate(
        self,
        actual: np.ndarray,
        predicted: np.ndarray,
    ) -> RegressionMetrics:
        return RegressionMetrics(
            mae=float(mean_absolute_error(actual, predicted)),
            rmse=float(np.sqrt(mean_squared_error(actual, predicted))),
            r2=float(r2_score(actual, predicted)),
        )
