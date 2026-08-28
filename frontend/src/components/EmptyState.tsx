import type { ReactNode } from "react";
import { Inbox } from "lucide-react";

interface EmptyStateProps {
  title: string;
  message: string;
  action?: ReactNode;
}

export function EmptyState({ title, message, action }: EmptyStateProps) {
  return (
    <div className="fera-surface flex flex-col items-center gap-3 rounded-[var(--fera-radius-lg)] p-8 text-center">
      <div className="flex h-12 w-12 items-center justify-center rounded-full bg-fera-surface-hover">
        <Inbox className="h-5 w-5 text-fera-text-muted" />
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
