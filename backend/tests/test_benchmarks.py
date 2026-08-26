from backend.app.models.benchmarks import RIDGE_FULL_VED_BENCHMARK


def test_ridge_full_ved_benchmark() -> None:
    benchmark = RIDGE_FULL_VED_BENCHMARK

    assert benchmark.model == "ridge"
    assert benchmark.mae == 0.279842
    assert benchmark.rmse == 0.659426
    assert benchmark.r2 == 0.842988
