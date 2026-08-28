import { PipelineStep } from "./PipelineStep";

const pipelineSteps = [
  "VED Dataset",
  "Archive Processing",
  "Record Mapping",
  "Preprocessing",
  "ML Dataset",
  "Feature Engineering",
  "Model Training",
  "Evaluation",
  "Production Artifact",
  "Prediction API",
];

export function PipelineVisualization() {
  return (
    <div className="fera-surface rounded-[var(--fera-radius-lg)] p-5">
      <h3 className="mb-4 text-sm font-semibold text-fera-text-primary">
        ML Pipeline
      </h3>
      <div className="flex flex-col gap-0">
        {pipelineSteps.map((step, i) => (
          <div key={i} className="relative">
            <PipelineStep
              label={step}
              index={i + 1}
              isLast={i === pipelineSteps.length - 1}
            />
            {i < pipelineSteps.length - 1 && (
              <div className="ml-4 h-5 w-px bg-fera-border" aria-hidden="true" />
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
