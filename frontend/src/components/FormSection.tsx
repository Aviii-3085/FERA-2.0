import type { ReactNode } from "react";

interface FormSectionProps {
  title: string;
  description?: string;
  children: ReactNode;
}

export function FormSection({
  title,
  description,
  children,
}: FormSectionProps) {
  return (
    <fieldset className="fera-surface fera-transition rounded-[var(--fera-radius-lg)] p-4 sm:p-5">
      <legend className="mb-3 flex items-center gap-2 px-1">
        <span className="text-sm font-semibold text-fera-text-primary">
          {title}
        </span>
      </legend>
      {description && (
        <p className="mb-3.5 text-xs text-fera-text-tertiary">{description}</p>
      )}
      <div className="grid grid-cols-1 gap-x-4 gap-y-4 sm:grid-cols-2">
        {children}
      </div>
    </fieldset>
  );
}
