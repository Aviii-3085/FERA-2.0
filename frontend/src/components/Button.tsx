import type { ButtonHTMLAttributes, ReactNode } from "react";

type ButtonVariant = "primary" | "secondary";
type ButtonSize = "sm" | "md";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  size?: ButtonSize;
  children: ReactNode;
}

const variantStyles: Record<ButtonVariant, string> = {
  primary:
    "bg-fera-accent text-fera-accent-contrast border-transparent shadow-[var(--fera-shadow-sm)] hover:bg-fera-accent-hover hover:shadow-[var(--fera-shadow-md)] active:bg-fera-accent-active",
  secondary:
    "bg-fera-surface text-fera-text-primary hover:bg-fera-surface-hover border-fera-border active:bg-fera-surface-hover",
};

const sizeStyles: Record<ButtonSize, string> = {
  sm: "px-3.5 py-1.5 text-xs rounded-[var(--fera-radius-sm)]",
  md: "px-4.5 py-2.5 text-sm rounded-[var(--fera-radius-md)]",
};

export function Button({
  variant = "primary",
  size = "md",
  className = "",
  children,
  disabled,
  ...props
}: ButtonProps) {
  return (
    <button
      className={`inline-flex items-center justify-center gap-2 border font-medium fera-transition fera-press fera-focus-ring disabled:cursor-not-allowed disabled:opacity-45 disabled:active:scale-100 disabled:shadow-none ${variantStyles[variant]} ${sizeStyles[size]} ${className}`}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
}
