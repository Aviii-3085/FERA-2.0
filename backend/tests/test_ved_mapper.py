from backend.app.data.ved_mapper import VEDRecordMapper


def test_mapper_maps_raw_ved_row() -> None:
    row = {
        "VehId": "457",
        "Trip": "1075",
        "Timestamp(ms)": "1000",
        "Vehicle Speed[km/h]": "45",
        "Engine RPM[RPM]": "1800",
        "OAT[DegC]": "20",
        "Air Conditioning Power[kW]": "1.2",
        "HV Battery Current[A]": "10",
        "HV Battery SOC[%]": "65",
        "HV Battery Voltage[V]": "350",
        "Fuel Rate[L/hr]": "0",
    }

    record = VEDRecordMapper().map(row)

    assert record.veh_id == 457
    assert record.trip == 1075
    assert record.speed_kmh == 45.0
    assert record.fuel_rate_lph == 0.0


def test_mapper_handles_missing_optional_values() -> None:
    row = {
        "VehId": "119",
        "Trip": "1184",
        "Timestamp(ms)": "0",
        "Vehicle Speed[km/h]": "40",
        "Engine RPM[RPM]": "1100",
        "OAT[DegC]": "10",
        "Air Conditioning Power[kW]": "NaN",
        "HV Battery Current[A]": "NaN",
        "HV Battery SOC[%]": "NaN",
        "HV Battery Voltage[V]": "NaN",
        "Fuel Rate[L/hr]": "5.5",
    }

    record = VEDRecordMapper().map(row)

    assert record.ac_power_kw is None
    assert record.hv_battery_current_a is None
    assert record.hv_battery_soc_pct is None
    assert record.hv_battery_voltage_v is None
    assert record.fuel_rate_lph == 5.5
