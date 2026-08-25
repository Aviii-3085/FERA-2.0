from pathlib import Path


class VEDDataSource:
    """Read-only access to the raw VED dataset."""

    def __init__(self, root: Path) -> None:
        self.root = root

    @property
    def dynamic_archives(self) -> list[Path]:
        data_dir = self.root / "Data"
        return sorted(data_dir.glob("VED_DynamicData_*.7z"))

    @property
    def static_files(self) -> list[Path]:
        data_dir = self.root / "Data"
        return sorted(data_dir.glob("VED_Static_Data_*.xlsx"))
