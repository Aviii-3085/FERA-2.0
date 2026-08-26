from pathlib import Path

import py7zr

from backend.app.data.ved_batch_preprocessor import VEDBatchPreprocessor


def test_weekly_member_discovery(tmp_path: Path) -> None:
    csv_names = [
        "VED_180328_week.csv",
        "VED_180404_week.csv",
        "README.txt",
    ]

    files = []

    for name in csv_names:
        path = tmp_path / name
        path.write_text("test", encoding="utf-8")
        files.append(path)

    archive_path = tmp_path / "test.7z"

    with py7zr.SevenZipFile(archive_path, mode="w") as archive:
        for path in files:
            archive.write(path, arcname=path.name)

    members = VEDBatchPreprocessor._weekly_members(archive_path)

    assert members == [
        "VED_180328_week.csv",
        "VED_180404_week.csv",
    ]
