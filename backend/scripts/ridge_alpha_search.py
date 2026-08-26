import pandas as pd
from pathlib import Path

from backend.app.data.efficiency_pipeline import EfficiencyMLPipeline
from backend.app.data.efficiency_feature_engineering import EfficiencyFeatureEngineer
from backend.app.data.vehicle_split import VehicleGroupedSplitter
from backend.app.models.efficiency_evaluator import EfficiencyEvaluator
from backend.app.models.ridge_tuning import RIDGE_ALPHAS, build_ridge


files = sorted(Path("data/processed/ved").glob("VED_*_week.csv"))

df = pd.concat(
    (pd.read_csv(f) for f in files),
    ignore_index=True,
)

X, y = EfficiencyMLPipeline().prepare_files(files)
X = EfficiencyFeatureEngineer().transform(X)

split = VehicleGroupedSplitter().split(df["veh_id"])
evaluator = EfficiencyEvaluator()

actual = y.iloc[split.test_indices].to_numpy()

rows = []

for alpha in RIDGE_ALPHAS:
    model = build_ridge(alpha)

    model.fit(
        X.iloc[split.train_indices],
        y.iloc[split.train_indices],
    )

    predicted = model.predict(
        X.iloc[split.test_indices]
    )

    metrics = evaluator.evaluate(actual, predicted)

    rows.append(
        {
            "alpha": alpha,
            "mae": metrics.mae,
            "rmse": metrics.rmse,
            "r2": metrics.r2,
        }
    )

result = pd.DataFrame(rows)

print(result.to_string(index=False))
