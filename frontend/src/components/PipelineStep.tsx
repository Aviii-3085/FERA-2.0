import { CircleCheck as CheckCircle2, Loader as Loader2, Circle } from "lucide-react";

type PipelineStepStatus = "complete" | "active" | "pending";

interface PipelineStepProps {
  label: string;
  index: number;
  isLast?: boolean;
  status?: PipelineStepStatus;
}

export function PipelineStep({
  label,
  index,
  isLast = false,
  status = "complete",
}: PipelineStepProps) {
  const icon = {
    complete: <CheckCircle2 className="h-4 w-4 text-fera-success" />,
    active: <Loader2 className="h-4 w-4 animate-spin text-fera-accent" />,
    pending: <Circle className="h-4 w-4 text-fera-text-muted" />,
  }[status];

  return (
    <div className="flex items-center gap-3">
      <div className="flex shrink-0 items-center gap-3">
        <span className="flex h-7 w-7 items-center justify-center rounded-full border border-fera-border bg-fera-surface text-xs font-mono font-medium text-fera-text-tertiary">
          {String(index).padStart(2, "0")}
        </span>
        {icon}
      </div>
      <span className="text-sm font-medium text-fera-text-primary">
        {label}
      </span>
      {!isLast && (
        <div className="ml-[14px] h-px flex-1 bg-fera-border" aria-hidden="true" />
      )}
    </div>
  );
}
