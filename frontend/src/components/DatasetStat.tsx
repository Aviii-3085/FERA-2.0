interface DatasetStatProps {
  label: string;
  value: string | number;
  unit?: string;
}

export function DatasetStat({ label, value, unit }: DatasetStatProps) {
  return (
    <div className="fera-surface rounded-lg p-4">
      <span className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary">
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
