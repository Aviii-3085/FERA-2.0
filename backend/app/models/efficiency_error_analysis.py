import pandas as pd


class EfficiencyErrorAnalyzer:
    """Analyze regression errors across fuel-rate ranges."""

    def by_range(
        self,
        actual: pd.Series,
        predicted,
    ) -> pd.DataFrame:
        frame = pd.DataFrame(
            {
                "actual": actual.to_numpy(),
                "predicted": predicted,
            }
        )

        frame["absolute_error"] = (
            frame["actual"] - frame["predicted"]
        ).abs()

        frame["range"] = pd.cut(
            frame["actual"],
            bins=[-float("inf"), 0, 1, 3, 6, float("inf")],
            labels=[
                "zero",
                "0-1",
                "1-3",
                "3-6",
                "6+",
            ],
            include_lowest=True,
        )

        return (
            frame.groupby("range", observed=False)
            .agg(
                rows=("actual", "size"),
                mae=("absolute_error", "mean"),
                actual_mean=("actual", "mean"),
                predicted_mean=("predicted", "mean"),
            )
            .reset_index()
        )
