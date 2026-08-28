import type { ReactNode } from "react";

interface DataTableProps {
  headers: string[];
  rows: (string | number | ReactNode)[][];
}

export function DataTable({ headers, rows }: DataTableProps) {
  return (
    <div className="fera-surface overflow-hidden rounded-[var(--fera-radius-lg)]">
      <div className="overflow-x-auto">
        <table className="w-full border-collapse">
          <thead>
            <tr className="border-b border-fera-border bg-fera-surface-hover/50">
              {headers.map((header, i) => (
                <th
                  key={i}
                  className="px-4 py-2.5 text-left text-[11px] font-semibold uppercase tracking-wider text-fera-text-tertiary"
                >
                  {header}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row, i) => (
              <tr
                key={i}
                className="border-b border-fera-border/50 fera-transition last:border-0 hover:bg-fera-surface-hover/60"
              >
                {row.map((cell, j) => (
                  <td
                    key={j}
                    className="px-4 py-2.5 text-sm text-fera-text-primary"
                  >
                    {typeof cell === "number" || typeof cell === "string" ? (
                      <span className="font-mono tabular-nums">{cell}</span>
                    ) : (
                      cell
                    )}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
