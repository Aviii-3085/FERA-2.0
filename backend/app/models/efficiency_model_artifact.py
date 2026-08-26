from pathlib import Path
import pickle

from backend.app.models.efficiency_artifact_metadata import (
    CURRENT_ARTIFACT_METADATA,
)
from backend.app.models.efficiency_artifact_validator import (
    EfficiencyArtifactValidator,
)


class EfficiencyModelArtifact:
    """Save and load trained efficiency model artifacts."""

    @staticmethod
    def save(
        model,
        feature_names: list[str],
        destination: Path,
        metadata=None,
    ) -> None:
        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if metadata is None:
            metadata = CURRENT_ARTIFACT_METADATA

        payload = {
            "model": model,
            "feature_names": feature_names,
            "metadata": metadata,
        }

        EfficiencyArtifactValidator.validate(payload)

        with destination.open("wb") as file:
            pickle.dump(payload, file)

    @staticmethod
    def load(destination: Path) -> dict:
        with destination.open("rb") as file:
            payload = pickle.load(file)

        EfficiencyArtifactValidator.validate(payload)

        return payload
