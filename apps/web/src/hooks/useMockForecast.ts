import forecast from "../mocks/mockForecast.json";
import type { ForecastPoint } from "../types";
export function useMockForecast() { return { points: forecast as ForecastPoint[] }; }
