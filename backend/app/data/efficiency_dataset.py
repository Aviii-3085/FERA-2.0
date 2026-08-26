from collections.abc import Iterable

import pandas as pd

from backend.app.data.efficiency_ml import EfficiencyMLRecord
from backend.app.data.ml_features import ML_FEATURES, ML_TARGET


class EfficiencyDatasetBuilder:
    """Build model-ready feature and target data."""

    def build(
        self,
        records: Iterable[EfficiencyMLRecord],
    ) -> tuple[pd.DataFrame, pd.Series]:
        rows = [record.model_dump() for record in records]

        frame = pd.DataFrame(rows)

        features = frame.loc[:, ML_FEATURES]
        target = frame.loc[:, ML_TARGET]

        return features, target
