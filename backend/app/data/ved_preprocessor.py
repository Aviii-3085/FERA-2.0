from collections.abc import Iterable
from pathlib import Path

from backend.app.data.ved import VEDDataSource
from backend.app.data.ved_contracts import VEDFuelRecord
from backend.app.data.ved_reader import VEDArchiveReader
from backend.app.data.ved_writer import VEDProcessedWriter


class VEDPreprocessor:
    """Convert selected raw VED archive members into normalized CSV data."""

    def __init__(
        self,
        reader: VEDArchiveReader | None = None,
        writer: VEDProcessedWriter | None = None,
    ) -> None:
        self.reader = reader or VEDArchiveReader()
        self.writer = writer or VEDProcessedWriter()

    def process_member(
        self,
        archive: Path,
        member: str,
        destination: Path,
    ) -> int:
        records: Iterable[VEDFuelRecord] = self.reader.read_member(
            archive,
            member,
        )

        return self.writer.write(records, destination)

    def process_first_dynamic_member(
        self,
        source: VEDDataSource,
        destination: Path,
    ) -> int:
        archives = source.dynamic_archives

        if not archives:
            raise FileNotFoundError("No VED dynamic archives found.")

        raise NotImplementedError(
            "Select a specific archive member explicitly."
        )
