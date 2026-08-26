import pandas as pd

from backend.app.models.efficiency_ridge import EfficiencyRidgeModel


def test_ridge_model_can_fit_and_predict() -> None:
    features = pd.DataFrame(
        {
            "speed_kmh": [20, 40, 60, 80],
            "engine_rpm": [1000, 1500, 2000, 2500],
        }
    )

    target = pd.Series([1.0, 2.0, 3.0, 4.0])

    model = EfficiencyRidgeModel()

    model.fit(features, target)
    predictions = model.predict(features)

    assert len(predictions) == 4
    assert (predictions >= 0).all()
