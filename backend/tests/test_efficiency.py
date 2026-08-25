from backend.app.schemas.efficiency import EfficiencyPrediction


def test_efficiency_prediction_accepts_valid_data() -> None:
    prediction = EfficiencyPrediction(
        fuel_rate_lph=6.5,
        confidence=0.92,
    )

    assert prediction.fuel_rate_lph == 6.5
    assert prediction.confidence == 0.92


def test_efficiency_prediction_rejects_invalid_confidence() -> None:
    try:
        EfficiencyPrediction(
            fuel_rate_lph=6.5,
            confidence=1.5,
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Confidence above 1 should be rejected")
