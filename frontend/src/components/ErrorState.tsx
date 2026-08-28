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
    <div className="fera-surface flex flex-col items-center gap-3 rounded-lg p-8 text-center">
      <AlertCircle className="h-8 w-8 text-fera-error" />
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
