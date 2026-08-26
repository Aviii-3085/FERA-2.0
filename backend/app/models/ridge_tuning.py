from sklearn.linear_model import Ridge


RIDGE_ALPHAS = (
    0.01,
    0.1,
    1.0,
    10.0,
    100.0,
)


def build_ridge(alpha: float) -> Ridge:
    return Ridge(alpha=alpha)
