from dataclasses import dataclass


@dataclass(frozen=True)
class EfficiencyArtifactMetadata:
    model_name: str
    model_version: str
    alpha: float
    feature_count: int
    prediction_constraint: str


CURRENT_ARTIFACT_METADATA = EfficiencyArtifactMetadata(
    model_name="ridge",
    model_version="1.0.0",
    alpha=1.0,
    feature_count=12,
    prediction_constraint="non_negative",
)
