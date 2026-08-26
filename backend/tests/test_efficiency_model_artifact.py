from pathlib import Path

import pandas as pd

from backend.app.models.efficiency_model_artifact import (
    EfficiencyModelArtifact,
)
from backend.app.models.efficiency_ridge import EfficiencyRidgeModel


def test_model_artifact_round_trip(tmp_path: Path) -> None:
    features = pd.DataFrame(
        {
            "speed_kmh": [10.0, 20.0, 30.0],
            "engine_rpm": [1000.0, 1500.0, 2000.0],
        }
    )

    target = pd.Series([1.0, 2.0, 3.0])

    model = EfficiencyRidgeModel()
    model.fit(features, target)

    destination = tmp_path / "efficiency_model.pkl"

    EfficiencyModelArtifact.save(
        model,
        list(features.columns),
        destination,
    )

    loaded = EfficiencyModelArtifact.load(destination)

    assert loaded["feature_names"] == list(features.columns)
    assert loaded["model"].predict(features).shape == (3,)
