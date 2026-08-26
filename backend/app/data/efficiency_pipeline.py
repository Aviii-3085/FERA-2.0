from pathlib import Path

import pandas as pd

from backend.app.data.efficiency_dataset import EfficiencyDatasetBuilder
from backend.app.data.efficiency_features import EfficiencyFeaturePreprocessor
from backend.app.data.efficiency_loader import EfficiencyDatasetLoader


class EfficiencyMLPipeline:
    """Build model-ready data from a processed VED CSV."""

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
        records = self.loader.load_file(path)
        features, target = self.builder.build(records)
        features = self.preprocessor.transform(features)

        return features, target
