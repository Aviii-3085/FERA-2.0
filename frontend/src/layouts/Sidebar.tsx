import { NavLink } from "react-router-dom";
import { LayoutDashboard, Calculator, Cpu, Database, Radio, Route, ChartBar as BarChart3, Car, X } from "lucide-react";
import { StatusIndicator } from "../components/StatusIndicator";
import type { SystemStatus } from "../types/api";

interface SidebarProps {
  isOpen: boolean;
  onClose: () => void;
  systemStatus: SystemStatus;
}

interface NavItem {
  label: string;
  to: string;
  icon: typeof LayoutDashboard;
  comingSoon?: boolean;
}

const primaryNav: NavItem[] = [
  { label: "Overview", to: "/overview", icon: LayoutDashboard },
  { label: "Prediction", to: "/prediction", icon: Calculator },
  { label: "Model", to: "/model", icon: Cpu },
  { label: "Dataset", to: "/dataset", icon: Database },
];

const futureNav: NavItem[] = [
  { label: "Live Telemetry", to: "/live-telemetry", icon: Radio, comingSoon: true },
  { label: "Trips", to: "/trips", icon: Route, comingSoon: true },
  { label: "Analytics", to: "/analytics", icon: BarChart3, comingSoon: true },
  { label: "Fleet", to: "/fleet", icon: Car, comingSoon: true },
];

export function Sidebar({ isOpen, onClose, systemStatus }: SidebarProps) {
  return (
    <>
      {isOpen && (
        <div
          className="fixed inset-0 z-30 bg-black/50 lg:hidden"
          onClick={onClose}
          aria-hidden="true"
        />
      )}

      <aside
        className={`fixed left-0 top-0 z-40 flex h-full w-64 flex-col border-r border-fera-border bg-fera-bg-elevated transition-transform duration-200 lg:translate-x-0 ${
          isOpen ? "translate-x-0" : "-translate-x-full"
        }`}
        aria-label="Primary navigation"
      >
        <div className="flex items-center justify-between border-b border-fera-border px-4 py-4">
          <div className="flex items-center gap-2.5">
            <div className="flex h-9 w-9 items-center justify-center rounded-md border border-fera-border-strong bg-fera-surface">
              <span className="font-mono text-sm font-bold text-fera-accent">
                F
              </span>
            </div>
            <div className="flex flex-col leading-tight">
              <span className="text-sm font-semibold text-fera-text-primary">
                FERA 2.0
              </span>
              <span className="text-[10px] text-fera-text-muted">
                Fuel Efficiency Research
              </span>
            </div>
          </div>
          <button
            onClick={onClose}
            className="inline-flex h-7 w-7 items-center justify-center rounded-md text-fera-text-secondary hover:bg-fera-surface-hover hover:text-fera-text-primary lg:hidden"
            aria-label="Close navigation"
          >
            <X className="h-4 w-4" />
          </button>
        </div>

        <nav className="flex-1 overflow-y-auto px-3 py-4">
          <div className="mb-2 px-2 text-[10px] font-medium uppercase tracking-wider text-fera-text-muted">
            Analysis
          </div>
          <div className="flex flex-col gap-0.5">
            {primaryNav.map((item) => {
              const Icon = item.icon;
              return (
                <NavLink
                  key={item.to}
                  to={item.to}
                  onClick={onClose}
                  className={({ isActive }) =>
                    `flex items-center gap-2.5 rounded-md px-2.5 py-2 text-sm font-medium transition-colors ${
                      isActive
                        ? "bg-fera-accent-muted text-fera-accent"
                        : "text-fera-text-secondary hover:bg-fera-surface-hover hover:text-fera-text-primary"
                    }`
                  }
                >
                  <Icon className="h-4 w-4 shrink-0" />
                  {item.label}
                </NavLink>
              );
            })}
          </div>

          <div className="mb-2 mt-6 px-2 text-[10px] font-medium uppercase tracking-wider text-fera-text-muted">
            Future Modules
          </div>
          <div className="flex flex-col gap-0.5">
            {futureNav.map((item) => {
              const Icon = item.icon;
              return (
                <div
                  key={item.to}
                  className="flex cursor-not-allowed items-center gap-2.5 rounded-md px-2.5 py-2 text-sm text-fera-text-muted"
                  aria-disabled="true"
                  title="Coming Soon"
                >
                  <Icon className="h-4 w-4 shrink-0 opacity-50" />
                  {item.label}
                  <span className="ml-auto rounded border border-fera-border px-1.5 py-0.5 text-[9px] font-medium uppercase tracking-wider text-fera-text-muted">
                    Soon
                  </span>
                </div>
              );
            })}
          </div>
        </nav>

        <div className="border-t border-fera-border px-4 py-3">
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-medium uppercase tracking-wider text-fera-text-muted">
              System
            </span>
            <StatusIndicator status={systemStatus} />
          </div>
        </div>
      </aside>
    </>
  );
}
