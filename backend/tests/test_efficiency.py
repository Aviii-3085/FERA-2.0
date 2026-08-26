from backend.app.schemas.efficiency import EfficiencyPrediction


def test_efficiency_prediction_accepts_valid_data() -> None:
    prediction = EfficiencyPrediction(
        fuel_rate_lph=6.5,
    )

    assert prediction.fuel_rate_lph == 6.5


def test_efficiency_prediction_rejects_negative_fuel_rate() -> None:
    try:
        EfficiencyPrediction(
            fuel_rate_lph=-1.0,
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Negative fuel rate should be rejected")
