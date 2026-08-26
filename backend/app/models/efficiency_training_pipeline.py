from pathlib import Path

import pandas as pd

from backend.app.data.efficiency_feature_engineering import (
    EfficiencyFeatureEngineer,
)
from backend.app.data.efficiency_pipeline import EfficiencyMLPipeline
from backend.app.data.vehicle_split import VehicleGroupedSplitter
from backend.app.models.efficiency_evaluator import EfficiencyEvaluator
from backend.app.models.efficiency_model_artifact import (
    EfficiencyModelArtifact,
)
from backend.app.models.efficiency_ridge import EfficiencyRidgeModel


class EfficiencyTrainingPipeline:
    """Reproducible training and evaluation pipeline."""

    def __init__(self) -> None:
        self.data_pipeline = EfficiencyMLPipeline()
        self.feature_engineer = EfficiencyFeatureEngineer()
        self.splitter = VehicleGroupedSplitter()
        self.evaluator = EfficiencyEvaluator()

    def train_and_evaluate(
        self,
        files: list[Path],
        artifact_path: Path | None = None,
    ) -> dict:
        frames = [
            pd.read_csv(file)
            for file in files
        ]

        dataframe = pd.concat(
            frames,
            ignore_index=True,
        )

        features, target = self.data_pipeline.prepare_files(files)
        features = self.feature_engineer.transform(features)

        split = self.splitter.split(
            dataframe["veh_id"]
        )

        model = EfficiencyRidgeModel()
        model.fit(
            features.iloc[split.train_indices],
            target.iloc[split.train_indices],
        )

        if artifact_path is not None:
            EfficiencyModelArtifact.save(
                model,
                list(features.columns),
                artifact_path,
            )

        predictions = model.predict(
            features.iloc[split.test_indices]
        )

        metrics = self.evaluator.evaluate(
            target.iloc[split.test_indices].to_numpy(),
            predictions,
        )

        return {
            "model": model,
            "metrics": metrics,
            "train_rows": len(split.train_indices),
            "test_rows": len(split.test_indices),
            "train_vehicles": dataframe.iloc[
                split.train_indices
            ]["veh_id"].nunique(),
            "test_vehicles": dataframe.iloc[
                split.test_indices
            ]["veh_id"].nunique(),
            "artifact_path": artifact_path,
        }
