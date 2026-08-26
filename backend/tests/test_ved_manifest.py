from pathlib import Path

from backend.app.data.ved_manifest import VEDManifestWriter


def test_manifest_writer_creates_manifest(tmp_path: Path) -> None:
    destination = tmp_path / "manifest.csv"

    entries = [
        {
            "source_archive": "VED_DynamicData_Part1.7z",
            "source_member": "VED_171101_week.csv",
            "processed_file": "VED_171101_week.csv",
            "records": 16073,
        }
    ]

    VEDManifestWriter().write(entries, destination)

    lines = destination.read_text(encoding="utf-8").splitlines()

    assert len(lines) == 2
    assert lines[0] == (
        "source_archive,source_member,processed_file,records"
    )
    assert "16073" in lines[1]
