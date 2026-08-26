from backend.app.data.ved_mapper import VEDRecordMapper


def test_mapper_normalizes_small_soc_rounding_overflow() -> None:
    row = {
        "VehId": "457",
        "Trip": "1075",
        "Timestamp(ms)": "0",
        "Vehicle Speed[km/h]": "45",
        "Engine RPM[RPM]": "1800",
        "OAT[DegC]": "20",
        "Air Conditioning Power[kW]": "1.2",
        "HV Battery Current[A]": "10",
        "HV Battery SOC[%]": "100.000030518",
        "HV Battery Voltage[V]": "350",
        "Fuel Rate[L/hr]": "0",
    }

    record = VEDRecordMapper().map(row)

    assert record.hv_battery_soc_pct == 100.0
