from collections.abc import Iterable
from pathlib import Path

import pandas as pd

from backend.app.data.efficiency_dataset import EfficiencyDatasetBuilder
from backend.app.data.efficiency_features import EfficiencyFeaturePreprocessor
from backend.app.data.efficiency_loader import EfficiencyDatasetLoader


class EfficiencyMLPipeline:
    """Build model-ready data from processed VED CSV files."""

    def __init__(
        self,
        loader: EfficiencyDatasetLoader | None = None,
        builder: EfficiencyDatasetBuilder | None = None,
        preprocessor: EfficiencyFeaturePreprocessor | None = None,
    ) -> None:
        self.loader = loader or EfficiencyDatasetLoader()
        self.builder = builder or EfficiencyDatasetBuilder()
        self.preprocessor = preprocessor or EfficiencyFeaturePreprocessor()

    def prepare(
        self,
        path: Path,
    ) -> tuple[pd.DataFrame, pd.Series]:
        return self.prepare_files([path])

    def prepare_files(
        self,
        paths: Iterable[Path],
    ) -> tuple[pd.DataFrame, pd.Series]:
        records = (
            record
            for path in paths
            for record in self.loader.load_file(path)
        )

        features, target = self.builder.build(records)
        features = self.preprocessor.transform(features)

        return features, target
