from pathlib import Path

import py7zr

from backend.app.data.ved import VEDDataSource
from backend.app.data.ved_preprocessor import VEDPreprocessor


class VEDBatchPreprocessor:
    """Process every weekly VED dynamic-data member."""

    def __init__(
        self,
        preprocessor: VEDPreprocessor | None = None,
    ) -> None:
        self.preprocessor = preprocessor or VEDPreprocessor()

    def process_all(
        self,
        source: VEDDataSource,
        destination: Path,
    ) -> dict[str, int]:
        destination.mkdir(parents=True, exist_ok=True)

        results: dict[str, int] = {}

        for archive in source.dynamic_archives:
            for member in self._weekly_members(archive):
                output_name = Path(member).with_suffix(".csv").name
                output = destination / output_name

                results[output_name] = self.preprocessor.process_member(
                    archive,
                    member,
                    output,
                )

        return results

    @staticmethod
    def _weekly_members(archive: Path) -> list[str]:
        with py7zr.SevenZipFile(archive, mode="r") as seven_zip:
            return sorted(
                name
                for name in seven_zip.getnames()
                if name.endswith("_week.csv")
            )
