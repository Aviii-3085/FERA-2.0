import pandas as pd
from pathlib import Path

from backend.app.data.efficiency_pipeline import EfficiencyMLPipeline
from backend.app.data.efficiency_feature_engineering import EfficiencyFeatureEngineer
from backend.app.data.vehicle_split import VehicleGroupedSplitter
from backend.app.models.efficiency_ridge import EfficiencyRidgeModel
from backend.app.models.efficiency_evaluator import EfficiencyEvaluator


files = sorted(Path("data/processed/ved").glob("VED_*_week.csv"))

df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)

X, y = EfficiencyMLPipeline().prepare_files(files)
X = EfficiencyFeatureEngineer().transform(X)

split = VehicleGroupedSplitter().split(df["veh_id"])
evaluator = EfficiencyEvaluator()

results = []

for feature in [None, *X.columns]:
    current = X if feature is None else X.drop(columns=[feature])

    model = EfficiencyRidgeModel()
    model.fit(
        current.iloc[split.train_indices],
        y.iloc[split.train_indices],
    )

    metrics = evaluator.evaluate(
        y.iloc[split.test_indices].to_numpy(),
        model.predict(current.iloc[split.test_indices]),
    )

    results.append(
        {
            "removed": "NONE" if feature is None else feature,
            "mae": metrics.mae,
            "rmse": metrics.rmse,
            "r2": metrics.r2,
        }
    )

print(
    pd.DataFrame(results)
    .sort_values("r2", ascending=False)
    .to_string(index=False)
)
