import pandas as pd

from backend.app.models.efficiency_error_analysis import (
    EfficiencyErrorAnalyzer,
)


def test_error_analyzer_groups_predictions_by_range() -> None:
    actual = pd.Series([0.0, 0.5, 2.0, 4.0, 8.0])
    predicted = [0.2, 0.6, 2.5, 3.0, 7.0]

    result = EfficiencyErrorAnalyzer().by_range(
        actual,
        predicted,
    )

    assert set(result["range"].astype(str)) == {
        "zero",
        "0-1",
        "1-3",
        "3-6",
        "6+",
    }

    assert result["rows"].sum() == 5
