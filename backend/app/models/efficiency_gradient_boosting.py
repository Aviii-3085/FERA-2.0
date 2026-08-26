from sklearn.ensemble import HistGradientBoostingRegressor


class EfficiencyGradientBoostingModel:
    """Gradient boosting fuel-rate regression model."""

    def __init__(
        self,
        random_state: int = 42,
    ) -> None:
        self.model = HistGradientBoostingRegressor(
            max_iter=200,
            learning_rate=0.08,
            max_leaf_nodes=31,
            random_state=random_state,
        )

    def fit(self, features, target) -> None:
        self.model.fit(features, target)

    def predict(self, features):
        return self.model.predict(features)
