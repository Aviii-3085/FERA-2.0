import numpy as np


class EfficiencyBiasAnalyzer:
    """Summarize systematic prediction bias."""

    def analyze(
        self,
        actual: np.ndarray,
        predicted: np.ndarray,
    ) -> dict[str, float]:
        error = predicted - actual

        return {
            "mean_error": float(np.mean(error)),
            "median_error": float(np.median(error)),
            "underprediction_rate": float(np.mean(error < 0)),
            "overprediction_rate": float(np.mean(error > 0)),
        }
