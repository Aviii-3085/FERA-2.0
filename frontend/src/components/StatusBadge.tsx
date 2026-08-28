import type { ReactNode } from "react";

type BadgeVariant = "neutral" | "success" | "warning" | "error" | "accent";

interface StatusBadgeProps {
  variant?: BadgeVariant;
  children: ReactNode;
}

const variantStyles: Record<BadgeVariant, string> = {
  neutral:
    "bg-fera-surface-hover text-fera-text-secondary border-fera-border",
  success:
    "bg-fera-success-muted text-fera-success border-fera-success/20",
  warning:
    "bg-fera-warning-muted text-fera-warning border-fera-warning/20",
  error: "bg-fera-error-muted text-fera-error border-fera-error/20",
  accent:
    "bg-fera-accent-muted text-fera-accent border-fera-accent/20",
};

export function StatusBadge({
  variant = "neutral",
  children,
}: StatusBadgeProps) {
  return (
    <span
      className={`inline-flex items-center gap-1.5 rounded-full border px-2.5 py-0.5 text-xs font-medium ${variantStyles[variant]}`}
    >
      {children}
    </span>
  );
}
