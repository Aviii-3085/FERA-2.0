from collections.abc import Iterable

import numpy as np
from sklearn.model_selection import GroupShuffleSplit

from backend.app.data.dataset_split import DatasetSplit


class VehicleGroupedSplitter:
    """Split observations while keeping each vehicle in one partition."""

    def split(
        self,
        groups: Iterable[int],
        test_size: float = 0.2,
        random_state: int = 42,
    ) -> DatasetSplit:
        groups_array = np.asarray(list(groups))
        indices = np.arange(len(groups_array))

        splitter = GroupShuffleSplit(
            n_splits=1,
            test_size=test_size,
            random_state=random_state,
        )

        train_idx, test_idx = next(
            splitter.split(indices, groups=groups_array)
        )

        return DatasetSplit(
            train_indices=train_idx,
            test_indices=test_idx,
        )
