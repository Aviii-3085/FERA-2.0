from backend.app.data.efficiency_feature_contract import ENGINEERED_FEATURES


def test_engineered_feature_contract() -> None:
    assert len(ENGINEERED_FEATURES) == 12
    assert "hv_battery_soc_pct" in ENGINEERED_FEATURES
    assert "hv_battery_voltage_v" in ENGINEERED_FEATURES
    assert "battery_power_kw" in ENGINEERED_FEATURES
