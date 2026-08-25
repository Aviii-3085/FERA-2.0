import csv
import tempfile
from collections.abc import Iterator
from pathlib import Path

import py7zr

from backend.app.data.ved_contracts import VEDFuelRecord
from backend.app.data.ved_mapper import VEDRecordMapper


class VEDArchiveReader:
    """Read fuel-rate records from VED 7z archives one member at a time."""

    def __init__(self, mapper: VEDRecordMapper | None = None) -> None:
        self.mapper = mapper or VEDRecordMapper()

    def read_member(
        self,
        archive: Path,
        member: str,
    ) -> Iterator[VEDFuelRecord]:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)

            with py7zr.SevenZipFile(archive, mode="r") as seven_zip:
                seven_zip.extract(
                    path=output_dir,
                    targets=[member],
                )

            csv_path = output_dir / member

            with csv_path.open(
                "r",
                encoding="utf-8",
                errors="replace",
                newline="",
            ) as stream:
                reader = csv.DictReader(stream)

                for row in reader:
                    fuel = row.get("Fuel Rate[L/hr]")

                    if self._is_missing(fuel):
                        continue

                    yield self.mapper.map(row)

    @staticmethod
    def _is_missing(value: object) -> bool:
        if value is None:
            return True

        return str(value).strip() in {
            "",
            "NaN",
            "nan",
            "NA",
            "N/A",
        }
