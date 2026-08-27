import type {
  HealthResponse,
  TelemetryInput,
  EfficiencyPrediction,
  PredictionError,
  PredictionErrorType,
} from "../types/api";

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

const PREDICT_TIMEOUT_MS = 15000;

function buildError(
  type: PredictionErrorType,
  message: string,
): PredictionError {
  return { type, message };
}

export const apiService = {
  async getHealth(signal?: AbortSignal): Promise<HealthResponse> {
    const response = await fetch(`${API_BASE_URL}/api/health`, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
      signal,
    });

    if (!response.ok) {
      throw new Error(`Health check failed: ${response.status}`);
    }

    return (await response.json()) as HealthResponse;
  },

  async predictEfficiency(
    input: TelemetryInput,
    signal?: AbortSignal,
  ): Promise<EfficiencyPrediction> {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), PREDICT_TIMEOUT_MS);

    const onAbort = () => controller.abort();
    signal?.addEventListener("abort", onAbort);

    try {
      const response = await fetch(`${API_BASE_URL}/api/efficiency/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(input),
        signal: controller.signal,
      });

      if (!response.ok) {
        const errorBody = await response.json().catch(() => null);

        if (response.status === 422) {
          throw buildError(
            "validation",
            "Please correct the highlighted telemetry fields.",
          );
        }

        if (response.status >= 500) {
          throw buildError(
            "server",
            "Prediction service returned an error. Please try again.",
          );
        }

        throw buildError(
          "server",
          errorBody?.detail ?? "Prediction service returned an error.",
        );
      }

      return (await response.json()) as EfficiencyPrediction;
    } catch (err) {
      if (err instanceof DOMException && err.name === "AbortError") {
        throw buildError(
          "timeout",
          "The prediction request timed out. Please try again.",
        );
      }

      if (err instanceof TypeError) {
        throw buildError(
          "network",
          "Unable to reach the FERA prediction service.",
        );
      }

      if (
        err !== null &&
        typeof err === "object" &&
        "type" in err &&
        "message" in err
      ) {
        throw err;
      }

      throw buildError(
        "unexpected",
        "An unexpected error occurred. Please try again.",
      );
    } finally {
      clearTimeout(timeoutId);
      signal?.removeEventListener("abort", onAbort);
    }
  },
};
