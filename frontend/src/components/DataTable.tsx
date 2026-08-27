import type { ReactNode } from "react";

interface DataTableProps {
  headers: string[];
  rows: (string | number | ReactNode)[][];
}

export function DataTable({ headers, rows }: DataTableProps) {
  return (
    <div className="fera-surface overflow-x-auto rounded-lg">
      <table className="w-full">
        <thead>
          <tr className="border-b border-fera-border">
            {headers.map((header, i) => (
              <th
                key={i}
                className="px-4 py-2.5 text-left text-xs font-medium uppercase tracking-wider text-fera-text-tertiary"
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
              className="border-b border-fera-border/50 last:border-0 transition-colors hover:bg-fera-surface-hover/50"
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
  );
}
