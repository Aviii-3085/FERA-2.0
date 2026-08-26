from fastapi.testclient import TestClient

from backend.app.main import app


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
