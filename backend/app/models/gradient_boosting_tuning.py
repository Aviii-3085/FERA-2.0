from itertools import product

from sklearn.ensemble import HistGradientBoostingRegressor


GRADIENT_BOOSTING_CONFIGS = tuple(
    {
        "max_iter": max_iter,
        "learning_rate": learning_rate,
        "max_leaf_nodes": max_leaf_nodes,
    }
    for max_iter, learning_rate, max_leaf_nodes in product(
        (100, 200, 300),
        (0.03, 0.08),
        (15, 31),
    )
)


def build_gradient_boosting(
    max_iter: int,
    learning_rate: float,
    max_leaf_nodes: int,
) -> HistGradientBoostingRegressor:
    return HistGradientBoostingRegressor(
        max_iter=max_iter,
        learning_rate=learning_rate,
        max_leaf_nodes=max_leaf_nodes,
        random_state=42,
    )
