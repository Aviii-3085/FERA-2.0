from fastapi.testclient import TestClient
import pytest

from backend.app.core.config import settings
from backend.app.main import app
from backend.app.services.efficiency import EfficiencyService


client = TestClient(app)


def test_efficiency_prediction_endpoint() -> None:
    response = client.post(
        "/api/efficiency/predict",
        json={
            "speed_kmh": 45.0,
            "engine_rpm": 1800.0,
            "outside_temperature_c": 25.0,
            "ac_power_kw": 1.5,
            "hv_battery_current_a": 20.0,
            "hv_battery_soc_pct": 70.0,
            "hv_battery_voltage_v": 350.0,
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "fuel_rate_lph" in body
    assert body["fuel_rate_lph"] >= 0


def test_efficiency_prediction_endpoint_rejects_invalid_input() -> None:
    response = client.post(
        "/api/efficiency/predict",
        json={
            "speed_kmh": -1.0,
            "engine_rpm": 1800.0,
            "outside_temperature_c": 25.0,
            "ac_power_kw": 1.5,
            "hv_battery_current_a": 20.0,
            "hv_battery_soc_pct": 70.0,
            "hv_battery_voltage_v": 350.0,
        },
    )

    assert response.status_code == 422
    
def test_efficiency_prediction_response_contract() -> None:
    response = client.post(
        "/api/efficiency/predict",
        json={
            "speed_kmh": 45.0,
            "engine_rpm": 1800.0,
            "outside_temperature_c": 25.0,
            "ac_power_kw": 1.5,
            "hv_battery_current_a": 20.0,
            "hv_battery_soc_pct": 70.0,
            "hv_battery_voltage_v": 350.0,
        },
    )

    assert response.status_code == 200
    assert response.headers["content-type"].startswith(
        "application/json"
    )

    body = response.json()

    assert set(body.keys()) == {"fuel_rate_lph"}
    assert isinstance(body["fuel_rate_lph"], float)
    assert body["fuel_rate_lph"] >= 0
    
def test_efficiency_prediction_complete_production_flow() -> None:
    response = client.post(
        "/api/efficiency/predict",
        json={
            "speed_kmh": 45.0,
            "engine_rpm": 1800.0,
            "outside_temperature_c": 25.0,
            "ac_power_kw": 1.5,
            "hv_battery_current_a": 20.0,
            "hv_battery_soc_pct": 70.0,
            "hv_battery_voltage_v": 350.0,
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["fuel_rate_lph"] == pytest.approx(
        4.513304470367185,
        abs=1e-9,
    )
    
def test_efficiency_prediction_rejects_invalid_physical_values() -> None:
    base_payload = {
        "speed_kmh": 45.0,
        "engine_rpm": 1800.0,
        "outside_temperature_c": 25.0,
        "ac_power_kw": 1.5,
        "hv_battery_current_a": 20.0,
        "hv_battery_soc_pct": 70.0,
        "hv_battery_voltage_v": 350.0,
    }

    invalid_cases = [
        ("speed_kmh", -1.0),
        ("engine_rpm", -1.0),
        ("ac_power_kw", -1.0),
        ("hv_battery_soc_pct", 101.0),
        ("hv_battery_voltage_v", -1.0),
    ]

    for field, value in invalid_cases:
        payload = base_payload.copy()
        payload[field] = value

        response = client.post(
            "/api/efficiency/predict",
            json=payload,
        )

        assert response.status_code == 422
    
def test_efficiency_prediction_rejects_missing_required_telemetry() -> None:
    response = client.post(
        "/api/efficiency/predict",
        json={
            "speed_kmh": 45.0,
            "engine_rpm": 1800.0,
            "outside_temperature_c": 25.0,
            "ac_power_kw": 1.5,
            "hv_battery_current_a": 20.0,
            "hv_battery_soc_pct": 70.0,
        },
    )

    assert response.status_code == 422
    
def test_efficiency_prediction_raises_when_model_artifact_is_missing() -> None:
    from pathlib import Path

    from backend.app.api import router

    original_service = router.efficiency_service

    router.efficiency_service = EfficiencyService(
        settings,
        artifact_path=Path(
            "data/models/does_not_exist.pkl"
        ),
    )

    try:
        with pytest.raises(FileNotFoundError):
            client.post(
                "/api/efficiency/predict",
                json={
                    "speed_kmh": 45.0,
                    "engine_rpm": 1800.0,
                    "outside_temperature_c": 25.0,
                    "ac_power_kw": 1.5,
                    "hv_battery_current_a": 20.0,
                    "hv_battery_soc_pct": 70.0,
                    "hv_battery_voltage_v": 350.0,
                },
            )
    finally:
        router.efficiency_service = original_service
