import csv
from collections.abc import Iterator
from pathlib import Path

from backend.app.data.efficiency_ml import EfficiencyMLRecord


class EfficiencyDatasetLoader:
    """Load normalized VED records for ML preparation."""

    def load_file(self, path: Path) -> Iterator[EfficiencyMLRecord]:
        with path.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as stream:
            reader = csv.DictReader(stream)

            for row in reader:
                yield EfficiencyMLRecord(
                    veh_id=int(row["veh_id"]),
                    trip=int(row["trip"]),
                    timestamp_ms=int(row["timestamp_ms"]),
                    speed_kmh=float(row["speed_kmh"]),
                    engine_rpm=float(row["engine_rpm"]),
                    outside_temperature_c=float(
                        row["outside_temperature_c"]
                    ),
                    ac_power_kw=self._optional_float(
                        row["ac_power_kw"]
                    ),
                    hv_battery_current_a=self._optional_float(
                        row["hv_battery_current_a"]
                    ),
                    hv_battery_soc_pct=self._optional_float(
                        row["hv_battery_soc_pct"]
                    ),
                    hv_battery_voltage_v=self._optional_float(
                        row["hv_battery_voltage_v"]
                    ),
                    fuel_rate_lph=float(row["fuel_rate_lph"]),
                )

    @staticmethod
    def _optional_float(value: str) -> float | None:
        if value.strip() == "":
            return None

        return float(value)
