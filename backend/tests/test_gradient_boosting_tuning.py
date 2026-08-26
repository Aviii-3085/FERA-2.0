from backend.app.models.gradient_boosting_tuning import (
    GRADIENT_BOOSTING_CONFIGS,
    build_gradient_boosting,
)


def test_gradient_boosting_tuning_candidates() -> None:
    assert len(GRADIENT_BOOSTING_CONFIGS) == 12

    for config in GRADIENT_BOOSTING_CONFIGS:
        model = build_gradient_boosting(**config)
        assert model.max_iter == config["max_iter"]
        assert model.learning_rate == config["learning_rate"]
        assert model.max_leaf_nodes == config["max_leaf_nodes"]
