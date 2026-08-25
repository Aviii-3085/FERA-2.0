from backend.app.data.contracts import DatasetInfo


def test_dataset_info() -> None:
    dataset = DatasetInfo(
        name="VED",
        source="University of Michigan",
        description="Vehicle Energy Dataset",
        license="Apache License 2.0",
    )

    assert dataset.name == "VED"
    assert dataset.license == "Apache License 2.0"
