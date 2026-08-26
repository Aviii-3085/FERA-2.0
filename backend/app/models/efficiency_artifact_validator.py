from backend.app.models.efficiency_artifact_metadata import (
    EfficiencyArtifactMetadata,
)


class EfficiencyArtifactValidator:
    """Validate the structure and metadata of an efficiency artifact."""

    @staticmethod
    def validate(payload: dict) -> None:
        required_keys = {
            "model",
            "feature_names",
            "metadata",
        }

        missing = required_keys - payload.keys()

        if missing:
            raise ValueError(
                f"Artifact missing keys: {sorted(missing)}"
            )

        metadata = payload["metadata"]

        if not isinstance(
            metadata,
            EfficiencyArtifactMetadata,
        ):
            raise ValueError(
                "Artifact metadata has an invalid type."
            )

        if metadata.model_name != "ridge":
            raise ValueError(
                f"Unsupported model: {metadata.model_name}"
            )

        if metadata.feature_count != len(
            payload["feature_names"]
        ):
            raise ValueError(
                "Feature count does not match feature names."
            )

        if metadata.prediction_constraint != "non_negative":
            raise ValueError(
                "Unsupported prediction constraint."
            )
