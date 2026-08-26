from pathlib import Path

from backend.app.data.efficiency_loader import EfficiencyDatasetLoader


def test_loader_reads_processed_ved_file(tmp_path: Path) -> None:
    path = tmp_path / "processed.csv"

    path.write_text(
        """veh_id,trip,timestamp_ms,speed_kmh,engine_rpm,outside_temperature_c,ac_power_kw,hv_battery_current_a,hv_battery_soc_pct,hv_battery_voltage_v,fuel_rate_lph
457,1075,0,45,1800,20,1.2,10,65,350,0
""",
        encoding="utf-8",
    )

    records = list(EfficiencyDatasetLoader().load_file(path))

    assert len(records) == 1
    assert records[0].veh_id == 457
    assert records[0].fuel_rate_lph == 0.0
