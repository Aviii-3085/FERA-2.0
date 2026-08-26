import pandas as pd

from backend.app.models.efficiency_gradient_boosting import (
    EfficiencyGradientBoostingModel,
)


def test_gradient_boosting_model_can_fit_and_predict() -> None:
    features = pd.DataFrame(
        {
            "speed_kmh": [10, 20, 30, 40, 50],
            "engine_rpm": [1000, 1500, 2000, 2500, 3000],
        }
    )

    target = pd.Series([1, 2, 3, 4, 5])

    model = EfficiencyGradientBoostingModel()
    model.fit(features, target)

    predictions = model.predict(features)

    assert len(predictions) == 5
