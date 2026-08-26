from pathlib import Path

from backend.app.data.efficiency_pipeline import EfficiencyMLPipeline


def test_ml_pipeline_prepares_processed_file(tmp_path: Path) -> None:
    path = tmp_path / "processed.csv"

    path.write_text(
        """veh_id,trip,timestamp_ms,speed_kmh,engine_rpm,outside_temperature_c,ac_power_kw,hv_battery_current_a,hv_battery_soc_pct,hv_battery_voltage_v,fuel_rate_lph
457,1075,0,45,1800,20,1.2,10,65,350,0
457,1075,200,46,1810,20,,11,65,350,5.5
""",
        encoding="utf-8",
    )

    features, target = EfficiencyMLPipeline().prepare(path)

    assert features.shape == (2, 7)
    assert features.isna().sum().sum() == 0
    assert target.tolist() == [0.0, 5.5]
