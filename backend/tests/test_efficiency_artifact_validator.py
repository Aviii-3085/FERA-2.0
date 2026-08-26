import pytest

from backend.app.models.efficiency_artifact_metadata import (
    CURRENT_ARTIFACT_METADATA,
)
from backend.app.models.efficiency_artifact_validator import (
    EfficiencyArtifactValidator,
)


def test_valid_artifact_passes() -> None:
    payload = {
        "model": object(),
        "feature_names": [
            f"feature_{index}"
            for index in range(12)
        ],
        "metadata": CURRENT_ARTIFACT_METADATA,
    }

    EfficiencyArtifactValidator.validate(payload)


def test_missing_artifact_key_fails() -> None:
    payload = {
        "model": object(),
        "feature_names": [],
    }

    with pytest.raises(ValueError):
        EfficiencyArtifactValidator.validate(payload)


def test_feature_count_mismatch_fails() -> None:
    payload = {
        "model": object(),
        "feature_names": ["feature"],
        "metadata": CURRENT_ARTIFACT_METADATA,
    }

    with pytest.raises(ValueError):
        EfficiencyArtifactValidator.validate(payload)
