import pandas as pd

from backend.app.models.efficiency_ridge import EfficiencyRidgeModel
from backend.app.models.ridge_feature_analysis import RidgeFeatureAnalyzer


def test_ridge_feature_analyzer_orders_coefficients() -> None:
    features = pd.DataFrame(
        {
            "speed_kmh": [10.0, 20.0, 30.0, 40.0],
            "engine_rpm": [1000.0, 1500.0, 2000.0, 2500.0],
        }
    )

    target = pd.Series([1.0, 2.0, 3.0, 4.0])

    model = EfficiencyRidgeModel()
    model.fit(features, target)

    result = RidgeFeatureAnalyzer().analyze(
        model,
        list(features.columns),
    )

    assert list(result.columns) == [
        "feature",
        "coefficient",
        "absolute_coefficient",
    ]
    assert len(result) == 2
    assert result["absolute_coefficient"].is_monotonic_decreasing
