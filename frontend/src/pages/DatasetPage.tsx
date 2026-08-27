import { Database } from "lucide-react";
import { PageHeader } from "../components/PageHeader";
import { DatasetStat } from "../components/DatasetStat";
import { MetadataRow } from "../components/MetadataRow";
import { PipelineVisualization } from "../components/PipelineVisualization";

export function DatasetPage() {
  return (
    <div className="flex flex-col gap-6">
      <PageHeader
        title="Dataset"
        description="Training data composition and ML pipeline architecture."
      />

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <DatasetStat label="Processed Records" value="896,097" />
        <DatasetStat label="Weekly VED Files" value="54" />
        <DatasetStat label="Vehicles with Fuel-Rate Data" value="13" />
        <DatasetStat label="Training Vehicles" value="10" />
        <DatasetStat label="Held-out Vehicles" value="3" />
      </div>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        <div className="fera-surface rounded-lg p-5">
          <div className="mb-4 flex items-center gap-2">
            <Database className="h-4 w-4 text-fera-accent" />
            <h3 className="text-sm font-semibold text-fera-text-primary">
              Dataset Summary
            </h3>
          </div>
          <div className="flex flex-col">
            <MetadataRow label="Total processed records" value="896,097" />
            <MetadataRow label="Weekly VED files" value="54" />
            <MetadataRow
              label="Vehicles with fuel-rate data"
              value="13"
            />
            <MetadataRow label="Training vehicles" value="10" />
            <MetadataRow label="Held-out vehicles" value="3" />
          </div>
          <div className="mt-4 border-t border-fera-border/50 pt-3">
            <p className="text-xs text-fera-text-muted">
              The dataset is derived from real VED vehicle telemetry. The
              vehicle-grouped evaluation ensures held-out vehicles are
              completely excluded from training, providing an unbiased
              estimate of model generalization.
            </p>
          </div>
        </div>

        <PipelineVisualization />
      </div>
    </div>
  );
}
