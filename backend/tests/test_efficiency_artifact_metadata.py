from backend.app.models.efficiency_artifact_metadata import (
    CURRENT_ARTIFACT_METADATA,
)


def test_current_artifact_metadata() -> None:
    metadata = CURRENT_ARTIFACT_METADATA

    assert metadata.model_name == "ridge"
    assert metadata.model_version == "1.0.0"
    assert metadata.alpha == 1.0
    assert metadata.feature_count == 12
    assert metadata.prediction_constraint == "non_negative"
