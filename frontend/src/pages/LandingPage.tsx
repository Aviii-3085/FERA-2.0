import { ArrowRight } from "lucide-react";
import { useNavigate } from "react-router-dom";

export function LandingPage() {
  const navigate = useNavigate();

  return (
    <div className="relative flex min-h-screen items-center justify-center overflow-hidden bg-fera-bg px-6 py-12">
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute -left-32 -top-32 h-96 w-96 rounded-full bg-fera-accent/15 blur-3xl" />
        <div className="absolute -right-32 top-1/4 h-96 w-96 rounded-full bg-fera-secondary/15 blur-3xl" />
        <div className="absolute -bottom-40 left-1/3 h-96 w-96 rounded-full bg-fera-success/10 blur-3xl" />
      </div>

      <div className="relative z-10 flex w-full max-w-5xl flex-col items-center text-center">
        <div className="mb-14 flex items-center justify-center">
          <img
            src="/branding/primary/fera-primary-light.png"
            alt="FERA — Fuel Efficiency Research & Analysis"
            className="h-auto w-[230px] object-contain drop-shadow-[0_12px_30px_rgba(0,0,0,0.12)] dark:hidden"
          />
          <img
            src="/branding/primary/fera-primary-dark.png"
            alt="FERA — Fuel Efficiency Research & Analysis"
            className="hidden h-auto w-[230px] object-contain drop-shadow-[0_12px_30px_rgba(0,0,0,0.25)] dark:block"
          />
        </div>

        <div className="w-full max-w-4xl">
          <p className="mb-6 text-xs font-semibold uppercase tracking-[0.3em] text-fera-accent">
            Fuel Efficiency Research & Analysis
          </p>

          <h1 className="mx-auto max-w-4xl text-4xl font-semibold leading-[1.08] tracking-[-0.02em] text-fera-text-primary sm:text-5xl lg:text-6xl">
            Fuel efficiency,
            <span className="block text-fera-text-secondary">
              measured with precision.
            </span>
          </h1>

          <p className="mx-auto mt-7 max-w-2xl text-sm leading-7 text-fera-text-secondary sm:text-base">
            Vehicle telemetry analysis and predictive modeling for real-world
            fuel performance.
          </p>

          <div className="mt-10 flex justify-center">
            <button
              onClick={() => navigate("/overview")}
              className="inline-flex items-center justify-center gap-2 rounded-[var(--fera-radius-md)] bg-fera-accent px-6 py-3 text-sm font-semibold text-fera-accent-contrast shadow-[var(--fera-shadow-md)] fera-transition fera-press fera-focus-ring hover:bg-fera-accent-hover hover:shadow-[var(--fera-shadow-lg)]"
            >
              View Analysis Workspace
              <ArrowRight className="h-4 w-4" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}