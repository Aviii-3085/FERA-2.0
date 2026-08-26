import numpy as np

from backend.app.models.efficiency_bias import EfficiencyBiasAnalyzer


def test_bias_analyzer() -> None:
    result = EfficiencyBiasAnalyzer().analyze(
        np.array([1.0, 2.0, 3.0]),
        np.array([0.5, 2.5, 2.0]),
    )

    assert result["mean_error"] == -1 / 3
    assert result["underprediction_rate"] == 2 / 3
    assert result["overprediction_rate"] == 1 / 3
