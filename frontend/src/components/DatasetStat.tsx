interface DatasetStatProps {
  label: string;
  value: string | number;
  unit?: string;
}

export function DatasetStat({ label, value, unit }: DatasetStatProps) {
  return (
    <div className="fera-surface fera-transition rounded-[var(--fera-radius-lg)] p-4 hover:border-fera-border-strong">
      <span className="text-[11px] font-semibold uppercase tracking-wider text-fera-text-tertiary">
        {label}
      </span>
      <div className="mt-1.5 flex items-baseline gap-1">
        <span className="font-mono text-xl font-semibold tabular-nums text-fera-text-primary">
          {value}
        </span>
        {unit && (
          <span className="text-sm font-medium text-fera-text-muted">
            {unit}
          </span>
        )}
      </div>
    </div>
  );
}
