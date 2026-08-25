from pathlib import Path

import py7zr

from backend.app.data.ved_reader import VEDArchiveReader


def test_reader_skips_missing_fuel_rows(tmp_path: Path) -> None:
    csv_content = """VehId,Trip,Timestamp(ms),Vehicle Speed[km/h],Engine RPM[RPM],OAT[DegC],Air Conditioning Power[kW],HV Battery Current[A],HV Battery SOC[%],HV Battery Voltage[V],Fuel Rate[L/hr]
457,1075,0,45,1800,20,1.2,10,65,350,0
457,1075,200,46,1810,20,1.2,11,65,350,5.5
457,1075,400,47,1820,20,1.2,12,65,350,NaN
"""

    csv_path = tmp_path / "VED_test_week.csv"
    csv_path.write_text(csv_content, encoding="utf-8")

    archive_path = tmp_path / "test.7z"

    with py7zr.SevenZipFile(archive_path, mode="w") as archive:
        archive.write(csv_path, arcname=csv_path.name)

    records = list(
        VEDArchiveReader().read_member(
            archive_path,
            csv_path.name,
        )
    )

    assert len(records) == 2
    assert records[0].fuel_rate_lph == 0.0
    assert records[1].fuel_rate_lph == 5.5
