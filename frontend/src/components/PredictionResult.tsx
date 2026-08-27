import { Loader as Loader2 } from "lucide-react";

interface PredictionResultProps {
  fuelRateLph: number;
  isLoading?: boolean;
}

export function PredictionResult({
  fuelRateLph,
  isLoading = false,
}: PredictionResultProps) {
  return (
    <div className="fera-surface relative overflow-hidden rounded-lg p-6">
      <div className="flex items-center justify-between">
        <span className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary">
          Predicted Fuel Rate
        </span>
        {isLoading && (
          <Loader2 className="h-4 w-4 animate-spin text-fera-accent" />
        )}
      </div>
      <div className="mt-3 flex items-baseline gap-2">
        <span className="font-mono text-4xl font-bold tabular-nums text-fera-accent sm:text-5xl">
          {isLoading ? "--" : fuelRateLph.toFixed(4)}
        </span>
        <span className="text-lg font-medium text-fera-text-secondary">
          L/hr
        </span>
      </div>
      <div className="mt-4 flex items-center gap-4 border-t border-fera-border/50 pt-3">
        <div className="flex flex-col">
          <span className="text-xs text-fera-text-muted">Model</span>
          <span className="text-sm font-medium text-fera-text-primary">
            Ridge Regression
          </span>
        </div>
        <div className="h-8 w-px bg-fera-border/50" />
        <div className="flex flex-col">
          <span className="text-xs text-fera-text-muted">Version</span>
          <span className="font-mono text-sm font-medium text-fera-text-primary">
            1.0.0
          </span>
        </div>
      </div>
    </div>
  );
}
