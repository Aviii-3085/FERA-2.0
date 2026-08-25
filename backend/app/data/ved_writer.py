import csv
from collections.abc import Iterable
from pathlib import Path

from backend.app.data.ved_contracts import VEDFuelRecord


class VEDProcessedWriter:
    """Write normalized VED fuel records to a processed CSV."""

    FIELDNAMES = [
        "veh_id",
        "trip",
        "timestamp_ms",
        "speed_kmh",
        "engine_rpm",
        "outside_temperature_c",
        "ac_power_kw",
        "hv_battery_current_a",
        "hv_battery_soc_pct",
        "hv_battery_voltage_v",
        "fuel_rate_lph",
    ]

    def write(
        self,
        records: Iterable[VEDFuelRecord],
        destination: Path,
    ) -> int:
        destination.parent.mkdir(parents=True, exist_ok=True)

        count = 0

        with destination.open(
            "w",
            encoding="utf-8",
            newline="",
        ) as stream:
            writer = csv.DictWriter(
                stream,
                fieldnames=self.FIELDNAMES,
            )

            writer.writeheader()

            for record in records:
                writer.writerow(record.model_dump())
                count += 1

        return count
