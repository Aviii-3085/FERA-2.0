from pathlib import Path

import py7zr

from backend.app.data.ved_preprocessor import VEDPreprocessor


def test_preprocessor_converts_selected_member(tmp_path: Path) -> None:
    csv_content = """VehId,Trip,Timestamp(ms),Vehicle Speed[km/h],Engine RPM[RPM],OAT[DegC],Air Conditioning Power[kW],HV Battery Current[A],HV Battery SOC[%],HV Battery Voltage[V],Fuel Rate[L/hr]
457,1075,0,45,1800,20,1.2,10,65,350,0
457,1075,200,46,1810,20,1.2,11,65,350,5.5
"""

    csv_path = tmp_path / "VED_test_week.csv"
    csv_path.write_text(csv_content, encoding="utf-8")

    archive_path = tmp_path / "test.7z"

    with py7zr.SevenZipFile(archive_path, mode="w") as archive:
        archive.write(csv_path, arcname=csv_path.name)

    destination = tmp_path / "processed" / "ved.csv"

    count = VEDPreprocessor().process_member(
        archive_path,
        csv_path.name,
        destination,
    )

    assert count == 2
    assert destination.exists()

    lines = destination.read_text(encoding="utf-8").splitlines()

    assert len(lines) == 3
    assert "457,1075,0" in lines[1]
    assert "457,1075,200" in lines[2]
