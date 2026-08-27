import { useLocation } from "react-router-dom";
import { Menu } from "lucide-react";
import { ThemeToggle } from "../components/ThemeToggle";
import { StatusIndicator } from "../components/StatusIndicator";
import type { SystemStatus, ThemeMode } from "../types/api";

interface HeaderProps {
  onMenuClick: () => void;
  systemStatus: SystemStatus;
  theme: ThemeMode;
  onToggleTheme: () => void;
}

const pageTitles: Record<string, { title: string; subtitle: string }> = {
  "/overview": { title: "Overview", subtitle: "System & model summary" },
  "/prediction": {
    title: "Prediction",
    subtitle: "Telemetry analysis workspace",
  },
  "/model": { title: "Model", subtitle: "Production model specification" },
  "/dataset": { title: "Dataset", subtitle: "Training data & pipeline" },
  "/": { title: "Overview", subtitle: "System & model summary" },
};

export function Header({
  onMenuClick,
  systemStatus,
  theme,
  onToggleTheme,
}: HeaderProps) {
  const location = useLocation();
  const page = pageTitles[location.pathname] ?? {
    title: "FERA",
    subtitle: "Fuel Efficiency Research & Analysis",
  };

  return (
    <header className="sticky top-0 z-20 flex h-14 items-center justify-between border-b border-fera-border bg-fera-bg/80 px-4 backdrop-blur-md lg:px-6">
      <div className="flex items-center gap-3">
        <button
          onClick={onMenuClick}
          className="inline-flex h-8 w-8 items-center justify-center rounded-md border border-fera-border bg-fera-surface text-fera-text-secondary hover:bg-fera-surface-hover lg:hidden"
          aria-label="Open navigation"
        >
          <Menu className="h-4 w-4" />
        </button>
        <div className="flex flex-col leading-tight">
          <h2 className="text-sm font-semibold text-fera-text-primary">
            {page.title}
          </h2>
          <span className="hidden text-xs text-fera-text-tertiary sm:block">
            {page.subtitle}
          </span>
        </div>
      </div>

      <div className="flex items-center gap-3">
        <div className="hidden sm:block">
          <StatusIndicator status={systemStatus} />
        </div>
        <ThemeToggle theme={theme} onToggle={onToggleTheme} />
      </div>
    </header>
  );
}
