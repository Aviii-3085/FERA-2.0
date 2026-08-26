import numpy as np


class MeanBaselineModel:
    """Predict the mean fuel rate observed in the training data."""

    def __init__(self) -> None:
        self.mean_: float | None = None

    def fit(self, target: np.ndarray) -> None:
        self.mean_ = float(np.mean(target))

    def predict(self, size: int) -> np.ndarray:
        if self.mean_ is None:
            raise RuntimeError("Model must be fitted before prediction.")

        return np.full(size, self.mean_)
