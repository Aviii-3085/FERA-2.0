import { Moon, Sun } from "lucide-react";
import type { ThemeMode } from "../types/api";

interface ThemeToggleProps {
  theme: ThemeMode;
  onToggle: () => void;
}

export function ThemeToggle({ theme, onToggle }: ThemeToggleProps) {
  return (
    <button
      onClick={onToggle}
      className="inline-flex h-8 w-8 items-center justify-center rounded-md border border-fera-border bg-fera-surface text-fera-text-secondary transition-colors hover:bg-fera-surface-hover hover:text-fera-text-primary fera-focus-ring"
      aria-label={`Switch to ${theme === "dark" ? "light" : "dark"} theme`}
      title={`Switch to ${theme === "dark" ? "light" : "dark"} theme`}
    >
      {theme === "dark" ? (
        <Sun className="h-4 w-4" />
      ) : (
        <Moon className="h-4 w-4" />
      )}
    </button>
  );
}
