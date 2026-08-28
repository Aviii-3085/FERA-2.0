import { useNavigate } from "react-router-dom";
import { ArrowRight, Cpu, Database, Activity } from "lucide-react";
import { PageHeader } from "../components/PageHeader";
import { MetricCard } from "../components/MetricCard";
import { MetadataRow } from "../components/MetadataRow";
import { Button } from "../components/Button";
import { StatusBadge } from "../components/StatusBadge";

export function OverviewPage() {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col gap-6">
      <PageHeader
        title="FERA 2.0"
        description="Fuel Efficiency Research & Analysis"
        actions={
          <Button onClick={() => navigate("/prediction")}>
            Run Prediction
            <ArrowRight className="h-4 w-4" />
          </Button>
        }
      />

      <div className="grid grid-cols-1 gap-4 md:grid-cols-3">
        <MetricCard
          label="MAE"
          value="0.190120"
          unit="L/hr"
          sublabel="Mean Absolute Error"
        />
        <MetricCard
          label="RMSE"
          value="0.611039"
          unit="L/hr"
          sublabel="Root Mean Square Error"
        />
        <MetricCard
          label="R²"
          value="0.865185"
          sublabel="Coefficient of Determination"
        />
      </div>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        <div className="fera-surface rounded-lg p-5">
          <div className="mb-4 flex items-center gap-2">
            <Cpu className="h-4 w-4 text-fera-accent" />
            <h3 className="text-sm font-semibold text-fera-text-primary">
              Production Model
            </h3>
            <StatusBadge variant="success">Active</StatusBadge>
          </div>
          <div className="flex flex-col">
            <MetadataRow label="Model" value="Ridge Regression" />
            <MetadataRow label="Version" value="1.0.0" />
            <MetadataRow label="Alpha" value="1.0" />
            <MetadataRow label="Features" value="12" />
            <MetadataRow label="Constraint" value="Non-negative" />
          </div>
        </div>

        <div className="fera-surface rounded-lg p-5">
          <div className="mb-4 flex items-center gap-2">
            <Database className="h-4 w-4 text-fera-accent" />
            <h3 className="text-sm font-semibold text-fera-text-primary">
              Dataset
            </h3>
          </div>
          <div className="flex flex-col">
            <MetadataRow label="Records" value="896,097" />
            <MetadataRow label="Vehicles" value="13" />
            <MetadataRow label="Training Vehicles" value="10" />
            <MetadataRow label="Held-out Vehicles" value="3" />
            <MetadataRow label="Locked Features" value="12" />
          </div>
        </div>
      </div>

      <div className="fera-surface rounded-lg p-5">
        <div className="mb-4 flex items-center gap-2">
          <Activity className="h-4 w-4 text-fera-accent" />
          <h3 className="text-sm font-semibold text-fera-text-primary">
            Prediction Workflow
          </h3>
        </div>
        <p className="mb-4 text-sm text-fera-text-secondary">
          Submit vehicle telemetry parameters to the production Ridge
          Regression model for real-time fuel rate prediction.
        </p>
        <Button onClick={() => navigate("/prediction")}>
          Open Prediction Workspace
          <ArrowRight className="h-4 w-4" />
        </Button>
      </div>
    </div>
  );
}
