from sklearn.ensemble import RandomForestRegressor


class EfficiencyBaselineModel:
    """Baseline fuel-rate regression model."""

    def __init__(
        self,
        random_state: int = 42,
    ) -> None:
        self.model = RandomForestRegressor(
            n_estimators=100,
            random_state=random_state,
            n_jobs=-1,
        )

    def fit(self, features, target) -> None:
        self.model.fit(features, target)

    def predict(self, features):
        return self.model.predict(features)
