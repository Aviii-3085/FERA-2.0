from backend.app.models.ridge_tuning import (
    RIDGE_ALPHAS,
    build_ridge,
)


def test_ridge_tuning_candidates() -> None:
    assert len(RIDGE_ALPHAS) == 5

    for alpha in RIDGE_ALPHAS:
        model = build_ridge(alpha)
        assert model.alpha == alpha
