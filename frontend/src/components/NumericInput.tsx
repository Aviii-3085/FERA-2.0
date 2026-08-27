import type { InputHTMLAttributes } from "react";

interface NumericInputProps
  extends Omit<InputHTMLAttributes<HTMLInputElement>, "type"> {
  label: string;
  unit?: string;
  error?: string | null;
  hint?: string;
}

export function NumericInput({
  label,
  unit,
  error,
  hint,
  id,
  className = "",
  ...props
}: NumericInputProps) {
  const inputId = id ?? props.name;

  return (
    <div className="flex flex-col gap-1">
      <div className="flex items-center justify-between">
        <label
          htmlFor={inputId}
          className="text-xs font-medium uppercase tracking-wider text-fera-text-tertiary"
        >
          {label}
        </label>
        {unit && (
          <span className="text-xs font-medium text-fera-text-muted">
            {unit}
          </span>
        )}
      </div>
      <input
        id={inputId}
        type="number"
        step="any"
        className={`w-full rounded-md border bg-fera-bg px-3 py-2 font-mono text-sm tabular-nums text-fera-text-primary transition-colors fera-focus-ring placeholder:text-fera-text-muted ${
          error
            ? "border-fera-error/50"
            : "border-fera-border hover:border-fera-border-strong"
        } ${className}`}
        aria-invalid={error ? true : undefined}
        aria-describedby={error ? `${inputId}-error` : undefined}
        {...props}
      />
      {error ? (
        <p
          id={`${inputId}-error`}
          className="text-xs text-fera-error"
          role="alert"
        >
          {error}
        </p>
      ) : hint ? (
        <p className="text-xs text-fera-text-muted">{hint}</p>
      ) : null}
    </div>
  );
}
