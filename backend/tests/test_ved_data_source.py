from pathlib import Path

from backend.app.data.ved import VEDDataSource


def test_ved_data_source_finds_raw_files() -> None:
    source = VEDDataSource(Path("data/raw/ved"))

    assert len(source.dynamic_archives) == 2
    assert len(source.static_files) == 2
    assert all(path.exists() for path in source.dynamic_archives)
    assert all(path.exists() for path in source.static_files)
