import { useCallback, useState } from "react";
import { apiService } from "../services/api";
import type {
  TelemetryInput,
  EfficiencyPrediction,
  PredictionError,
} from "../types/api";

interface PredictionState {
  isLoading: boolean;
  result: EfficiencyPrediction | null;
  error: PredictionError | null;
}

export function usePrediction() {
  const [state, setState] = useState<PredictionState>({
    isLoading: false,
    result: null,
    error: null,
  });

  const predict = useCallback(async (input: TelemetryInput) => {
    setState({ isLoading: true, result: null, error: null });

    try {
      const result = await apiService.predictEfficiency(input);
      setState({ isLoading: false, result, error: null });
    } catch (err) {
      const error =
        err !== null &&
        typeof err === "object" &&
        "type" in err &&
        "message" in err
          ? (err as PredictionError)
          : ({
              type: "unexpected",
              message: "An unexpected error occurred. Please try again.",
            } satisfies PredictionError);

      setState({ isLoading: false, result: null, error });
    }
  }, []);

  const reset = useCallback(() => {
    setState({ isLoading: false, result: null, error: null });
  }, []);

  return { ...state, predict, reset };
}
