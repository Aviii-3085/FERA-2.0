from pathlib import Path

import pandas as pd

from backend.app.models.efficiency_artifact_metadata import (
    CURRENT_ARTIFACT_METADATA,
)
from backend.app.data.efficiency_feature_contract import (
    ENGINEERED_FEATURES,
)
from backend.app.models.efficiency_model_artifact import (
    EfficiencyModelArtifact,
)
from backend.app.models.efficiency_ridge import EfficiencyRidgeModel


def test_model_artifact_round_trip(tmp_path: Path) -> None:
    features = pd.DataFrame(
        {
            feature: [1.0, 2.0, 3.0]
            for feature in ENGINEERED_FEATURES
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
    assert loaded["metadata"] == CURRENT_ARTIFACT_METADATA
    assert loaded["model"].predict(features).shape == (3,)
