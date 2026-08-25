from pathlib import Path

from backend.app.data.ved_contracts import VEDFuelRecord
from backend.app.data.ved_writer import VEDProcessedWriter


def test_writer_creates_normalized_csv(tmp_path: Path) -> None:
    destination = tmp_path / "ved_processed.csv"

    records = [
        VEDFuelRecord(
            veh_id=457,
            trip=1075,
            timestamp_ms=0,
            speed_kmh=45,
            engine_rpm=1800,
            outside_temperature_c=20,
            ac_power_kw=1.2,
            hv_battery_current_a=10,
            hv_battery_soc_pct=65,
            hv_battery_voltage_v=350,
            fuel_rate_lph=0,
        ),
        VEDFuelRecord(
            veh_id=457,
            trip=1075,
            timestamp_ms=200,
            speed_kmh=46,
            engine_rpm=1810,
            outside_temperature_c=20,
            ac_power_kw=1.2,
            hv_battery_current_a=11,
            hv_battery_soc_pct=65,
            hv_battery_voltage_v=350,
            fuel_rate_lph=5.5,
        ),
    ]

    count = VEDProcessedWriter().write(records, destination)

    assert count == 2
    assert destination.exists()

    lines = destination.read_text(encoding="utf-8").splitlines()

    assert len(lines) == 3
    assert lines[0].startswith("veh_id,trip,timestamp_ms")
    assert ",0.0" in lines[1]
    assert ",5.5" in lines[2]
