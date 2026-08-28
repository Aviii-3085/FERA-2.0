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
    <div className="fera-surface fera-transition relative overflow-hidden rounded-[var(--fera-radius-lg)] p-4 hover:border-fera-border-strong hover:shadow-[var(--fera-shadow-md)]">
      <div className="flex items-start justify-between gap-2">
        <span className="text-[11px] font-semibold uppercase tracking-wider text-fera-text-tertiary">
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
