import numpy as np

from backend.app.models.efficiency_evaluator import EfficiencyEvaluator


def test_evaluator_calculates_regression_metrics() -> None:
    actual = np.array([1.0, 2.0, 3.0])
    predicted = np.array([1.0, 2.0, 4.0])

    metrics = EfficiencyEvaluator().evaluate(actual, predicted)

    assert metrics.mae > 0
    assert metrics.rmse > 0
    assert metrics.r2 < 1.0
