from sklearn.linear_model import Ridge


class EfficiencyRidgeModel:
    """Regularized linear fuel-rate baseline."""

    def __init__(
        self,
        alpha: float = 1.0,
    ) -> None:
        self.model = Ridge(alpha=alpha)

    def fit(self, features, target) -> None:
        self.model.fit(features, target)

    def predict(self, features):
        return self.model.predict(features)
