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
          className="fixed inset-0 z-30 bg-black/40 backdrop-blur-[2px] fera-transition lg:hidden"
          onClick={onClose}
          aria-hidden="true"
        />
      )}

      <aside
        className={`fixed left-0 top-0 z-40 flex h-full w-72 flex-col border-r border-fera-border bg-fera-bg-elevated transition-transform duration-300 ease-[cubic-bezier(0.32,0.72,0,1)] lg:translate-x-0 ${
          isOpen ? "translate-x-0" : "-translate-x-full"
        }`}
        aria-label="Primary navigation"
      >
        <div className="flex items-center justify-between border-b border-fera-border px-5 py-4">
          <div className="flex items-center gap-2.5">
            <img
              src="/branding/mark/fera-mark-light.png"
              alt="FERA"
              className="h-10 w-10 rounded-[var(--fera-radius-sm)] object-contain"
            />
            <div className="flex flex-col leading-tight">
              <span className="text-sm font-semibold text-fera-text-primary">
                FERA 2.0
              </span>
              <span className="text-[11px] text-fera-text-muted">
                Fuel Efficiency Research & Analysis
              </span>
            </div>
          </div>
          <button
            onClick={onClose}
            className="inline-flex h-8 w-8 items-center justify-center rounded-full text-fera-text-secondary fera-transition fera-press hover:bg-fera-surface-hover hover:text-fera-text-primary lg:hidden"
            aria-label="Close navigation"
          >
            <X className="h-4 w-4" />
          </button>
        </div>

        <nav className="flex-1 overflow-y-auto px-3.5 py-5">
          <div className="mb-2 px-2.5 text-[10px] font-semibold uppercase tracking-wider text-fera-text-muted">
            Analysis
          </div>
          <div className="flex flex-col gap-1">
            {primaryNav.map((item) => {
              const Icon = item.icon;
              return (
                <NavLink
                  key={item.to}
                  to={item.to}
                  onClick={onClose}
                  className={({ isActive }) =>
                    `flex items-center gap-3 rounded-[var(--fera-radius-sm)] px-3 py-2.5 text-sm font-medium fera-transition ${
                      isActive
                        ? "bg-fera-accent-muted text-fera-accent shadow-[var(--fera-shadow-xs)]"
                        : "text-fera-text-secondary hover:bg-fera-surface-hover hover:text-fera-text-primary"
                    }`
                  }
                >
                  {({ isActive }) => (
                    <>
                      <span
                        className={`flex h-7 w-7 shrink-0 items-center justify-center rounded-full fera-transition ${
                          isActive ? "bg-fera-accent text-fera-accent-contrast" : "text-fera-text-tertiary"
                        }`}
                      >
                        <Icon className="h-4 w-4" />
                      </span>
                      {item.label}
                    </>
                  )}
                </NavLink>
              );
            })}
          </div>

          <div className="mb-2 mt-7 px-2.5 text-[10px] font-semibold uppercase tracking-wider text-fera-text-muted">
            Future Modules
          </div>
          <div className="flex flex-col gap-1">
            {futureNav.map((item) => {
              const Icon = item.icon;
              return (
                <div
                  key={item.to}
                  className="flex cursor-not-allowed items-center gap-3 rounded-[var(--fera-radius-sm)] px-3 py-2.5 text-sm text-fera-text-muted"
                  aria-disabled="true"
                  title="Coming Soon"
                >
                  <span className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-fera-surface-hover/60 opacity-60">
                    <Icon className="h-4 w-4" />
                  </span>
                  {item.label}
                  <span className="ml-auto rounded-full bg-fera-warning-muted px-2 py-0.5 text-[9px] font-semibold uppercase tracking-wider text-fera-warning">
                    Soon
                  </span>
                </div>
              );
            })}
          </div>
        </nav>

        <div className="border-t border-fera-border px-5 py-3.5">
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-semibold uppercase tracking-wider text-fera-text-muted">
              System
            </span>
            <StatusIndicator status={systemStatus} />
          </div>
        </div>
      </aside>
    </>
  );
}