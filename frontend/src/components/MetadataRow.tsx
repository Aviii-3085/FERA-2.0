interface MetadataRowProps {
  label: string;
  value: string | number;
  unit?: string;
}

export function MetadataRow({ label, value, unit }: MetadataRowProps) {
  return (
    <div className="flex items-center justify-between border-b border-fera-border/50 py-2 last:border-0">
      <span className="text-sm text-fera-text-secondary">{label}</span>
      <span className="font-mono text-sm font-medium tabular-nums text-fera-text-primary">
        {value}
        {unit && (
          <span className="ml-1 text-xs text-fera-text-muted">{unit}</span>
        )}
      </span>
    </div>
  );
}
