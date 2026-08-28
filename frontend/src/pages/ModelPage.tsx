import { Cpu, Lock } from "lucide-react";
import { PageHeader } from "../components/PageHeader";
import { MetricCard } from "../components/MetricCard";
import { MetadataRow } from "../components/MetadataRow";
import { DataTable } from "../components/DataTable";
import { StatusBadge } from "../components/StatusBadge";

interface FeatureInfo {
  index: number;
  name: string;
  category: "API" | "Engineered";
}

const apiFeatures: FeatureInfo[] = [
  { index: 1, name: "speed_kmh", category: "API" },
  { index: 2, name: "engine_rpm", category: "API" },
  { index: 3, name: "outside_temperature_c", category: "API" },
  { index: 4, name: "ac_power_kw", category: "API" },
  { index: 5, name: "hv_battery_current_a", category: "API" },
  { index: 6, name: "hv_battery_soc_pct", category: "API" },
  { index: 7, name: "hv_battery_voltage_v", category: "API" },
];

const engineeredFeatures: FeatureInfo[] = [
  { index: 8, name: "speed_squared", category: "Engineered" },
  { index: 9, name: "engine_rpm_squared", category: "Engineered" },
  { index: 10, name: "speed_rpm_interaction", category: "Engineered" },
  { index: 11, name: "battery_power_kw", category: "Engineered" },
  { index: 12, name: "speed_ac_interaction", category: "Engineered" },
];

export function ModelPage() {
  return (
    <div className="flex flex-col gap-6">
      <PageHeader
        title="Model"
        description="Production model specification and feature contract."
      />

      <div className="grid grid-cols-1 gap-4 md:grid-cols-4">
        <MetricCard label="Model" value="Ridge Regression" />
        <MetricCard label="Version" value="1.0.0" />
        <MetricCard label="Alpha" value="1.0" />
        <MetricCard label="Features" value="12" />
      </div>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        <div className="fera-surface rounded-lg p-5">
          <div className="mb-4 flex items-center gap-2">
            <Cpu className="h-4 w-4 text-fera-accent" />
            <h3 className="text-sm font-semibold text-fera-text-primary">
              Model Specification
            </h3>
          </div>
          <div className="flex flex-col">
            <MetadataRow label="Model" value="Ridge Regression" />
            <MetadataRow label="Version" value="1.0.0" />
            <MetadataRow label="Alpha" value="1.0" />
            <MetadataRow label="Feature Count" value="12" />
            <MetadataRow label="Prediction Constraint" value="Non-negative" />
          </div>
        </div>

        <div className="fera-surface rounded-lg p-5">
          <h3 className="mb-4 text-sm font-semibold text-fera-text-primary">
            Official Benchmark
          </h3>
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
            <div className="fera-surface-hover rounded-md p-3">
              <span className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary">
                MAE
              </span>
              <div className="mt-1 flex items-baseline gap-1">
                <span className="font-mono text-lg font-semibold tabular-nums text-fera-text-primary">
                  0.190120
                </span>
                <span className="text-xs text-fera-text-muted">L/hr</span>
              </div>
            </div>
            <div className="fera-surface-hover rounded-md p-3">
              <span className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary">
                RMSE
              </span>
              <div className="mt-1 flex items-baseline gap-1">
                <span className="font-mono text-lg font-semibold tabular-nums text-fera-text-primary">
                  0.611039
                </span>
                <span className="text-xs text-fera-text-muted">L/hr</span>
              </div>
            </div>
            <div className="fera-surface-hover rounded-md p-3">
              <span className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary">
                R²
              </span>
              <div className="mt-1">
                <span className="font-mono text-lg font-semibold tabular-nums text-fera-text-primary">
                  0.865185
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="fera-surface rounded-lg p-5">
        <h3 className="mb-4 text-sm font-semibold text-fera-text-primary">
          Evaluation
        </h3>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
          <div>
            <span className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary">
              Method
            </span>
            <p className="mt-1 text-sm text-fera-text-primary">
              Vehicle-grouped evaluation
            </p>
          </div>
          <div>
            <span className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary">
              Training Vehicles
            </span>
            <p className="mt-1 font-mono text-sm font-medium text-fera-text-primary">
              10
            </p>
          </div>
          <div>
            <span className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary">
              Held-out Vehicles
            </span>
            <p className="mt-1 font-mono text-sm font-medium text-fera-text-primary">
              3
            </p>
          </div>
        </div>
        <div className="mt-3 border-t border-fera-border/50 pt-3">
          <span className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary">
            Vehicles with fuel-rate data
          </span>
          <p className="mt-1 font-mono text-sm font-medium text-fera-text-primary">
            13
          </p>
        </div>
      </div>

      <div className="fera-surface rounded-lg p-5">
        <div className="mb-4 flex items-center gap-2">
          <Lock className="h-4 w-4 text-fera-accent" />
          <h3 className="text-sm font-semibold text-fera-text-primary">
            Feature Contract — 12 Locked Features
          </h3>
        </div>

        <div className="mb-4">
          <div className="mb-2 flex items-center gap-2">
            <h4 className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary">
              API / User Inputs
            </h4>
            <StatusBadge variant="accent">7 fields</StatusBadge>
          </div>
          <p className="mb-3 text-xs text-fera-text-muted">
            These seven features are provided by the user via the prediction
            API.
          </p>
          <DataTable
            headers={["#", "Feature Name"]}
            rows={apiFeatures.map((f) => [f.index, f.name])}
          />
        </div>

        <div>
          <div className="mb-2 flex items-center gap-2">
            <h4 className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary">
              Engineered Features
            </h4>
            <StatusBadge variant="neutral">5 fields</StatusBadge>
          </div>
          <p className="mb-3 text-xs text-fera-text-muted">
            These five features are engineered internally by the backend
            feature-engineering pipeline. They are not exposed as user input
            fields.
          </p>
          <DataTable
            headers={["#", "Feature Name"]}
            rows={engineeredFeatures.map((f) => [f.index, f.name])}
          />
        </div>
      </div>
    </div>
  );
}
