import type { ReactNode } from "react";

interface MetricCardProps {
  label: string;
  value: string | number;
  unit?: string;
  sublabel?: string;
  children?: ReactNode;
}

export function MetricCard({
  label,
  value,
  unit,
  sublabel,
  children,
}: MetricCardProps) {
  return (
    <div className="fera-surface relative overflow-hidden rounded-lg p-4 transition-colors hover:border-fera-border-strong">
      <div className="flex items-start justify-between gap-2">
        <span className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary">
          {label}
        </span>
        {children}
      </div>
      <div className="mt-2 flex items-baseline gap-1">
        <span className="font-mono text-2xl font-semibold tabular-nums text-fera-text-primary">
          {value}
        </span>
        {unit && (
          <span className="text-sm font-medium text-fera-text-tertiary">
            {unit}
          </span>
        )}
      </div>
      {sublabel && (
        <p className="mt-1 text-xs text-fera-text-muted">{sublabel}</p>
      )}
    </div>
  );
}
