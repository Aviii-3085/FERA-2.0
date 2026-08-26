from pathlib import Path
import pickle


class EfficiencyModelArtifact:
    """Save and load trained efficiency model artifacts."""

    @staticmethod
    def save(
        model,
        feature_names: list[str],
        destination: Path,
    ) -> None:
        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        payload = {
            "model": model,
            "feature_names": feature_names,
        }

        with destination.open("wb") as file:
            pickle.dump(payload, file)

    @staticmethod
    def load(destination: Path) -> dict:
        with destination.open("rb") as file:
            return pickle.load(file)
