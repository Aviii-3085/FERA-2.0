interface MetricDisplayProps {
  label: string;
  value: string | number;
  unit?: string;
}

export function MetricDisplay({ label, value, unit }: MetricDisplayProps) {
  return (
    <div className="flex flex-col gap-0.5">
      <span className="text-[11px] font-semibold uppercase tracking-wider text-fera-text-tertiary">
        {label}
      </span>
      <div className="flex items-baseline gap-1">
        <span className="font-mono text-base font-semibold tabular-nums text-fera-text-primary">
          {value}
        </span>
        {unit && (
          <span className="text-xs font-medium text-fera-text-muted">
            {unit}
          </span>
        )}
      </div>
    </div>
  );
}
