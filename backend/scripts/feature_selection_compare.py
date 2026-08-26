import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from backend.app.data.efficiency_pipeline import EfficiencyMLPipeline
from backend.app.data.efficiency_feature_engineering import EfficiencyFeatureEngineer
from backend.app.data.vehicle_split import VehicleGroupedSplitter
from backend.app.models.efficiency_ridge import EfficiencyRidgeModel

files = sorted(Path("data/processed/ved").glob("VED_*_week.csv"))
df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)

X, y = EfficiencyMLPipeline().prepare_files(files)
X = EfficiencyFeatureEngineer().transform(X)

split = VehicleGroupedSplitter().split(df["veh_id"])

test_df = df.iloc[split.test_indices].copy()
test_df["actual"] = y.iloc[split.test_indices].to_numpy()

for removed in [
    "NONE",
    "hv_battery_soc_pct",
    "hv_battery_voltage_v",
]:
    current = X if removed == "NONE" else X.drop(columns=[removed])

    model = EfficiencyRidgeModel()
    model.fit(
        current.iloc[split.train_indices],
        y.iloc[split.train_indices],
    )

    test_df["predicted"] = model.predict(
        current.iloc[split.test_indices]
    )

    print(f"\nRemoved: {removed}")

    for vehicle, group in test_df.groupby("veh_id"):
        mae = mean_absolute_error(group["actual"], group["predicted"])
        rmse = np.sqrt(
            mean_squared_error(group["actual"], group["predicted"])
        )
        r2 = r2_score(group["actual"], group["predicted"])

        print(
            f"Vehicle {vehicle}: "
            f"MAE={mae:.6f} "
            f"RMSE={rmse:.6f} "
            f"R2={r2:.6f}"
        )
