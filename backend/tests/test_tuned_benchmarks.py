from backend.app.models.tuned_benchmarks import (
    GRADIENT_BOOSTING_BEST,
    RIDGE_FINAL,
)


def test_tuned_benchmarks() -> None:
    assert RIDGE_FINAL.model == "ridge"
    assert RIDGE_FINAL.parameters["alpha"] == 1.0
    assert RIDGE_FINAL.r2 == 0.858363

    assert GRADIENT_BOOSTING_BEST.model == "gradient_boosting"
    assert GRADIENT_BOOSTING_BEST.parameters["max_iter"] == 100
    assert GRADIENT_BOOSTING_BEST.parameters["learning_rate"] == 0.03
    assert GRADIENT_BOOSTING_BEST.parameters["max_leaf_nodes"] == 15
