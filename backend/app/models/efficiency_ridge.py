import numpy as np
from sklearn.linear_model import Ridge


class EfficiencyRidgeModel:
    """Regularized linear fuel-rate model with non-negative predictions."""

    def __init__(
        self,
        alpha: float = 1.0,
    ) -> None:
        self.model = Ridge(alpha=alpha)

    def fit(self, features, target) -> None:
        self.model.fit(features, target)

    def predict(self, features):
        predictions = self.model.predict(features)
        return np.maximum(predictions, 0.0)
