from pathlib import Path

from backend.app.models.efficiency_training_pipeline import (
    EfficiencyTrainingPipeline,
)


def test_training_pipeline(tmp_path: Path) -> None:
    files = [
        Path("data/processed/ved/VED_180328_week.csv"),
    ]

    artifact = tmp_path / "efficiency_model.pkl"

    result = EfficiencyTrainingPipeline().train_and_evaluate(
        files,
        artifact,
    )

    assert result["train_rows"] > 0
    assert result["test_rows"] > 0
    assert result["train_vehicles"] > 0
    assert result["test_vehicles"] > 0
    assert result["model"] is not None
    assert result["metrics"].mae >= 0
    assert result["metrics"].rmse >= 0
    assert result["artifact_path"] == artifact
    assert artifact.exists()
