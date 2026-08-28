import type { ReactNode } from "react";
import { CircleAlert as AlertCircle } from "lucide-react";

interface ErrorStateProps {
  title?: string;
  message: string;
  action?: ReactNode;
}

export function ErrorState({
  title = "Error",
  message,
  action,
}: ErrorStateProps) {
  return (
    <div className="fera-surface flex flex-col items-center gap-3 rounded-[var(--fera-radius-lg)] p-8 text-center">
      <div className="flex h-12 w-12 items-center justify-center rounded-full bg-fera-error-muted">
        <AlertCircle className="h-5 w-5 text-fera-error" />
      </div>
      <div>
        <h3 className="text-sm font-semibold text-fera-text-primary">
          {title}
        </h3>
        <p className="mt-1 text-sm text-fera-text-secondary">{message}</p>
      </div>
      {action && <div className="mt-1">{action}</div>}
    </div>
  );
}
