import csv
from pathlib import Path


class VEDManifestWriter:
    """Create a manifest describing processed VED weekly datasets."""

    FIELDNAMES = [
        "source_archive",
        "source_member",
        "processed_file",
        "records",
    ]

    def write(
        self,
        entries: list[dict[str, str | int]],
        destination: Path,
    ) -> None:
        destination.parent.mkdir(parents=True, exist_ok=True)

        with destination.open(
            "w",
            encoding="utf-8",
            newline="",
        ) as stream:
            writer = csv.DictWriter(
                stream,
                fieldnames=self.FIELDNAMES,
            )
            writer.writeheader()
            writer.writerows(entries)
