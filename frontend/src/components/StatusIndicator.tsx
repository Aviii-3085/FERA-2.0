import type { SystemStatus } from "../types/api";

interface StatusIndicatorProps {
  status: SystemStatus;
  size?: "sm" | "md";
}

const statusConfig: Record<
  SystemStatus,
  { color: string; label: string; ring: string }
> = {
  online: {
    color: "bg-fera-success",
    label: "Online",
    ring: "shadow-[0_0_0_4px_var(--fera-success-muted)]",
  },
  unavailable: {
    color: "bg-fera-error",
    label: "Unavailable",
    ring: "shadow-[0_0_0_4px_var(--fera-error-muted)]",
  },
  checking: {
    color: "bg-fera-warning",
    label: "Checking",
    ring: "shadow-[0_0_0_4px_var(--fera-warning-muted)]",
  },
};

export function StatusIndicator({ status, size = "sm" }: StatusIndicatorProps) {
  const config = statusConfig[status];
  const dotSize = size === "sm" ? "h-2 w-2" : "h-2.5 w-2.5";

  return (
    <span className="inline-flex items-center gap-2">
      <span
        className={`${dotSize} rounded-full fera-transition ${config.color} ${config.ring} ${status === "checking" ? "animate-pulse" : ""}`}
        aria-hidden="true"
      />
      <span
        className={
          size === "sm"
            ? "text-xs font-medium text-fera-text-secondary"
            : "text-sm font-medium text-fera-text-secondary"
        }
      >
        {config.label}
      </span>
    </span>
  );
}
