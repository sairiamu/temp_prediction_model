import forecast from "../mocks/mockForecast.json";
import { ForecastChart } from "../components/charts/ForecastChart";
import type { ForecastPoint } from "../types";
export function Forecast() { return <div className="card"><h2>Multi-output horizon</h2><ForecastChart points={forecast as ForecastPoint[]} /></div>; }
