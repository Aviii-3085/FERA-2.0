from backend.app.data.vehicle_split import VehicleGroupedSplitter


def test_split_keeps_vehicles_separate() -> None:
    groups = [
        1, 1, 1,
        2, 2,
        3, 3, 3,
        4, 4,
        5, 5,
    ]

    result = VehicleGroupedSplitter().split(
        groups,
        test_size=0.4,
        random_state=42,
    )

    train_vehicles = {groups[i] for i in result.train_indices}
    test_vehicles = {groups[i] for i in result.test_indices}

    assert train_vehicles.isdisjoint(test_vehicles)
    assert (
        result.train_indices.size + result.test_indices.size
        == len(groups)
    )
