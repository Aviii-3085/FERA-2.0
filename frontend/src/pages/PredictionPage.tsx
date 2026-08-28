import { useState, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { Send } from "lucide-react";
import { PageHeader } from "../components/PageHeader";
import { FormSection } from "../components/FormSection";
import { NumericInput } from "../components/NumericInput";
import { Button } from "../components/Button";
import { PredictionResult } from "../components/PredictionResult";
import { ErrorState } from "../components/ErrorState";
import { usePrediction } from "../hooks/usePrediction";
import type { TelemetryInput } from "../types/api";

interface FieldErrors {
  speed_kmh?: string;
  engine_rpm?: string;
  outside_temperature_c?: string;
  ac_power_kw?: string;
  hv_battery_current_a?: string;
  hv_battery_soc_pct?: string;
  hv_battery_voltage_v?: string;
}

const defaultValues: TelemetryInput = {
  speed_kmh: 45,
  engine_rpm: 1800,
  outside_temperature_c: 25,
  ac_power_kw: 1.5,
  hv_battery_current_a: 20,
  hv_battery_soc_pct: 70,
  hv_battery_voltage_v: 350,
};

function validateField(name: keyof TelemetryInput, value: number): string | undefined {
  if (isNaN(value)) return "Must be a valid number.";

  switch (name) {
    case "speed_kmh":
      if (value < 0) return "Speed must be >= 0.";
      break;
    case "engine_rpm":
      if (value < 0) return "Engine RPM must be >= 0.";
      break;
    case "ac_power_kw":
      if (value < 0) return "AC power must be >= 0.";
      break;
    case "hv_battery_soc_pct":
      if (value < 0) return "SOC must be >= 0.";
      if (value > 100) return "SOC must be <= 100.";
      break;
    case "hv_battery_voltage_v":
      if (value < 0) return "Voltage must be >= 0.";
      break;
  }

  return undefined;
}

function validateAll(input: TelemetryInput): FieldErrors {
  const errors: FieldErrors = {};
  (Object.keys(input) as (keyof TelemetryInput)[]).forEach((key) => {
    const error = validateField(key, input[key]);
    if (error) errors[key] = error;
  });
  return errors;
}

export function PredictionPage() {
  const navigate = useNavigate();
  const { isLoading, result, error, predict } = usePrediction();
  const [values, setValues] = useState<TelemetryInput>(defaultValues);
  const [errors, setErrors] = useState<FieldErrors>({});

  const handleChange = useCallback(
    (name: keyof TelemetryInput, rawValue: string) => {
      const value = rawValue === "" ? NaN : Number(rawValue);
      setValues((prev) => ({ ...prev, [name]: value }));
      setErrors((prev) => ({
        ...prev,
        [name]: validateField(name, value),
      }));
    },
    [],
  );

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const validationErrors = validateAll(values);
    setErrors(validationErrors);

    if (Object.keys(validationErrors).length > 0) return;

    void predict(values);
  };

  const hasErrors = Object.values(errors).some((v) => v !== undefined);

  return (
    <div className="flex flex-col gap-6 sm:gap-7">
      <PageHeader
        title="Prediction"
        description="Telemetry analysis workspace — submit vehicle parameters to the production model."
      />

      <div className="grid grid-cols-1 gap-6 lg:grid-cols-5">
        <form
          onSubmit={handleSubmit}
          className="flex flex-col gap-4 lg:col-span-3"
        >
          <FormSection
            title="Vehicle Dynamics"
            description="Powertrain and motion telemetry."
          >
            <NumericInput
              name="speed_kmh"
              label="Speed"
              unit="km/h"
              value={Number.isNaN(values.speed_kmh) ? "" : values.speed_kmh}
              error={errors.speed_kmh}
              onChange={(e) => handleChange("speed_kmh", e.target.value)}
            />
            <NumericInput
              name="engine_rpm"
              label="Engine RPM"
              unit="RPM"
              value={Number.isNaN(values.engine_rpm) ? "" : values.engine_rpm}
              error={errors.engine_rpm}
              onChange={(e) => handleChange("engine_rpm", e.target.value)}
            />
          </FormSection>

          <FormSection
            title="Environment"
            description="External conditions affecting efficiency."
          >
            <NumericInput
              name="outside_temperature_c"
              label="Outside Temperature"
              unit="°C"
              value={
                Number.isNaN(values.outside_temperature_c)
                  ? ""
                  : values.outside_temperature_c
              }
              error={errors.outside_temperature_c}
              hint="Negative values are valid."
              onChange={(e) =>
                handleChange("outside_temperature_c", e.target.value)
              }
            />
          </FormSection>

          <FormSection
            title="Electrical System"
            description="HV battery and accessory power parameters."
          >
            <NumericInput
              name="ac_power_kw"
              label="AC Power"
              unit="kW"
              value={Number.isNaN(values.ac_power_kw) ? "" : values.ac_power_kw}
              error={errors.ac_power_kw}
              onChange={(e) => handleChange("ac_power_kw", e.target.value)}
            />
            <NumericInput
              name="hv_battery_current_a"
              label="HV Battery Current"
              unit="A"
              value={
                Number.isNaN(values.hv_battery_current_a)
                  ? ""
                  : values.hv_battery_current_a
              }
              error={errors.hv_battery_current_a}
              hint="Negative values are valid."
              onChange={(e) =>
                handleChange("hv_battery_current_a", e.target.value)
              }
            />
            <NumericInput
              name="hv_battery_soc_pct"
              label="HV Battery SOC"
              unit="%"
              value={
                Number.isNaN(values.hv_battery_soc_pct)
                  ? ""
                  : values.hv_battery_soc_pct
              }
              error={errors.hv_battery_soc_pct}
              onChange={(e) =>
                handleChange("hv_battery_soc_pct", e.target.value)
              }
            />
            <NumericInput
              name="hv_battery_voltage_v"
              label="HV Battery Voltage"
              unit="V"
              value={
                Number.isNaN(values.hv_battery_voltage_v)
                  ? ""
                  : values.hv_battery_voltage_v
              }
              error={errors.hv_battery_voltage_v}
              onChange={(e) =>
                handleChange("hv_battery_voltage_v", e.target.value)
              }
            />
          </FormSection>

          <div className="flex items-center gap-3">
            <Button
              type="submit"
              disabled={isLoading || hasErrors}
              className="min-w-[180px]"
            >
              {isLoading ? (
                <>
                  <span className="h-4 w-4 fera-spin-slow rounded-full border-2 border-fera-accent-contrast/30 border-t-fera-accent-contrast" />
                  Predicting...
                </>
              ) : (
                <>
                  <Send className="h-4 w-4" />
                  Predict Fuel Rate
                </>
              )}
            </Button>
            <Button
              type="button"
              variant="secondary"
              onClick={() => navigate("/overview")}
            >
              Cancel
            </Button>
          </div>
        </form>

        <div className="flex flex-col gap-4 lg:col-span-2">
          <div>
            <h3 className="mb-3 text-sm font-semibold text-fera-text-primary">
              Result
            </h3>
            {isLoading ? (
              <PredictionResult fuelRateLph={0} isLoading />
            ) : result ? (
              <PredictionResult fuelRateLph={result.fuel_rate_lph} />
            ) : error ? (
              <ErrorState
                title={
                  error.type === "validation"
                    ? "Validation Error"
                    : error.type === "network"
                      ? "Connection Error"
                      : error.type === "timeout"
                        ? "Request Timeout"
                        : "Prediction Error"
                }
                message={error.message}
              />
            ) : (
              <div className="fera-surface flex flex-col items-center gap-2 rounded-[var(--fera-radius-lg)] p-8 text-center">
                <p className="text-sm text-fera-text-secondary">
                  No prediction yet.
                </p>
                <p className="text-xs text-fera-text-muted">
                  Submit telemetry parameters to get a fuel rate prediction.
                </p>
              </div>
            )}
          </div>

          <div className="fera-surface rounded-[var(--fera-radius-lg)] p-4">
            <h4 className="mb-2 text-[11px] font-semibold uppercase tracking-wider text-fera-text-tertiary">
              Example Values
            </h4>
            <p className="text-xs text-fera-text-muted">
              The form is pre-populated with example telemetry inputs for
              demonstration. These are not live vehicle readings.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
