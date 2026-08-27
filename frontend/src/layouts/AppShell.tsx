import { useState } from "react";
import type { ReactNode } from "react";
import { Sidebar } from "./Sidebar";
import { Header } from "./Header";
import { useHealth } from "../hooks/useHealth";
import { useTheme } from "../hooks/useTheme";

interface AppShellProps {
  children: ReactNode;
}

export function AppShell({ children }: AppShellProps) {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const { status } = useHealth();
  const { theme, toggleTheme } = useTheme();

  return (
    <div className="min-h-screen bg-fera-bg">
      <Sidebar
        isOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
        systemStatus={status}
      />
      <div className="lg:pl-64">
        <Header
          onMenuClick={() => setSidebarOpen(true)}
          systemStatus={status}
          theme={theme}
          onToggleTheme={toggleTheme}
        />
        <main className="mx-auto max-w-7xl px-4 py-6 lg:px-8">{children}</main>
      </div>
    </div>
  );
}
