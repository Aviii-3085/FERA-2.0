from collections.abc import Mapping

from backend.app.data.ved_contracts import VEDFuelRecord


class VEDRecordMapper:
    """Map a raw VED row into the FERA fuel-record contract."""

    def map(self, row: Mapping[str, object]) -> VEDFuelRecord:
        return VEDFuelRecord(
            veh_id=int(float(row["VehId"])),
            trip=int(float(row["Trip"])),
            timestamp_ms=int(float(row["Timestamp(ms)"])),
            speed_kmh=float(row["Vehicle Speed[km/h]"]),
            engine_rpm=float(row["Engine RPM[RPM]"]),
            outside_temperature_c=float(row["OAT[DegC]"]),
            ac_power_kw=self._optional_float(
                row.get("Air Conditioning Power[kW]")
            ),
            hv_battery_current_a=self._optional_float(
                row.get("HV Battery Current[A]")
            ),
            hv_battery_soc_pct=self._normalize_soc(
                row.get("HV Battery SOC[%]")
            ),
            hv_battery_voltage_v=self._optional_float(
                row.get("HV Battery Voltage[V]")
            ),
            fuel_rate_lph=float(row["Fuel Rate[L/hr]"]),
        )

    @staticmethod
    def _optional_float(value: object) -> float | None:
        if value is None:
            return None

        text = str(value).strip()

        if text in {"", "NaN", "nan", "NA", "N/A"}:
            return None

        return float(text)
    @classmethod
    def _normalize_soc(cls, value: object) -> float | None:
        value = cls._optional_float(value)

        if value is None:
            return None

        if 100 < value <= 100.01:
            return 100.0

        return value
