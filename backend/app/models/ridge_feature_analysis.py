import pandas as pd


class RidgeFeatureAnalyzer:
    """Analyze Ridge feature coefficients."""

    def analyze(
        self,
        model,
        feature_names: list[str] | tuple[str, ...],
    ) -> pd.DataFrame:
        return (
            pd.DataFrame(
                {
                    "feature": feature_names,
                    "coefficient": model.model.coef_,
                }
            )
            .assign(
                absolute_coefficient=lambda frame:
                frame["coefficient"].abs()
            )
            .sort_values(
                "absolute_coefficient",
                ascending=False,
            )
            .reset_index(drop=True)
        )
