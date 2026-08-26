import numpy as np

from backend.app.models.mean_baseline import MeanBaselineModel


def test_mean_baseline_predicts_training_mean() -> None:
    target = np.array([1.0, 2.0, 3.0])

    model = MeanBaselineModel()
    model.fit(target)

    predictions = model.predict(3)

    assert predictions.tolist() == [2.0, 2.0, 2.0]
