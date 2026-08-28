import { Loader as Loader2 } from "lucide-react";

interface LoadingStateProps {
  message?: string;
}

export function LoadingState({
  message = "Loading...",
}: LoadingStateProps) {
  return (
    <div className="flex items-center justify-center gap-3 py-12">
      <Loader2 className="h-5 w-5 animate-spin text-fera-accent" />
      <span className="text-sm text-fera-text-secondary">{message}</span>
    </div>
  );
}
