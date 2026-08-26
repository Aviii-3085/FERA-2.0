from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class DatasetSplit:
    train_indices: np.ndarray
    test_indices: np.ndarray
