export interface HealthResponse {
  status: string;
  project: string;
  version: string;
}

export interface TelemetryInput {
  speed_kmh: number;
  engine_rpm: number;
  outside_temperature_c: number;
  ac_power_kw: number;
  hv_battery_current_a: number;
  hv_battery_soc_pct: number;
  hv_battery_voltage_v: number;
}

export interface EfficiencyPrediction {
  fuel_rate_lph: number;
}

export type PredictionErrorType =
  | "validation"
  | "network"
  | "server"
  | "timeout"
  | "unexpected";

export interface PredictionError {
  type: PredictionErrorType;
  message: string;
}

export type SystemStatus = "online" | "unavailable" | "checking";

export type ThemeMode = "dark" | "light";
