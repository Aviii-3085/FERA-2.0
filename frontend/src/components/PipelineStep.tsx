import { CircleCheck as CheckCircle2, Loader as Loader2, Circle } from "lucide-react";

type PipelineStepStatus = "complete" | "active" | "pending";

interface PipelineStepProps {
  label: string;
  index: number;
  isLast?: boolean;
  status?: PipelineStepStatus;
}

const badgeStyles: Record<PipelineStepStatus, string> = {
  complete: "bg-fera-success-muted text-fera-success",
  active: "bg-fera-accent-muted text-fera-accent",
  pending: "bg-fera-surface-hover text-fera-text-muted",
};

export function PipelineStep({
  label,
  index,
  isLast = false,
  status = "complete",
}: PipelineStepProps) {
  const icon = {
    complete: <CheckCircle2 className="h-3.5 w-3.5" />,
    active: <Loader2 className="h-3.5 w-3.5 fera-spin-slow" />,
    pending: <Circle className="h-3.5 w-3.5" />,
  }[status];

  return (
    <div className="flex items-center gap-3">
      <div className="flex shrink-0 items-center gap-3">
        <span
          className={`flex h-8 w-8 items-center justify-center rounded-full fera-transition ${badgeStyles[status]}`}
        >
          {icon}
        </span>
        <span className="font-mono text-[11px] font-medium text-fera-text-muted">
          {String(index).padStart(2, "0")}
        </span>
      </div>
      <span className="text-sm font-medium text-fera-text-primary">
        {label}
      </span>
      {!isLast && (
        <div className="ml-[2px] h-px flex-1 bg-fera-border" aria-hidden="true" />
      )}
    </div>
  );
}
