import { useCallback, useEffect, useRef, useState } from "react";
import { apiService } from "../services/api";
import type { HealthResponse, SystemStatus } from "../types/api";

interface HealthState {
  status: SystemStatus;
  data: HealthResponse | null;
  error: string | null;
}

const POLL_INTERVAL_MS = 30000;

export function useHealth() {
  const [state, setState] = useState<HealthState>({
    status: "checking",
    data: null,
    error: null,
  });

  const abortRef = useRef<AbortController | null>(null);

  const checkHealth = useCallback(async () => {
    abortRef.current?.abort();
    const controller = new AbortController();
    abortRef.current = controller;

    try {
      const data = await apiService.getHealth(controller.signal);
      setState({
        status: data.status === "ok" ? "online" : "unavailable",
        data,
        error: null,
      });
    } catch {
      setState((prev) => ({
        ...prev,
        status: "unavailable",
        error: "Unable to reach the FERA API.",
      }));
    }
  }, []);

  useEffect(() => {
    const timer = setTimeout(() => void checkHealth(), 0);
    const interval = setInterval(() => void checkHealth(), POLL_INTERVAL_MS);

    return () => {
      clearTimeout(timer);
      clearInterval(interval);
      abortRef.current?.abort();
    };
  }, [checkHealth]);

  return { ...state, refresh: checkHealth };
}
