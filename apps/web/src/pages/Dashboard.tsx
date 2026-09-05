import forecast from "../mocks/mockForecast.json";
import loss from "../mocks/mockLossCurve.json";
import anomalies from "../mocks/mockAnomalies.json";
import { ForecastChart } from "../components/charts/ForecastChart";
import { LossChart } from "../components/charts/LossChart";
import { AnomalyChart } from "../components/charts/AnomalyChart";
import { GlassCard } from "../components/ui/GlassCard";
import type { AnomalyPoint, ForecastPoint, LossPoint } from "../types";
export function Dashboard() { return <div className="grid"><GlassCard title="Forecast"><ForecastChart points={forecast as ForecastPoint[]} /></GlassCard><GlassCard title="Training loss"><LossChart points={loss as LossPoint[]} /></GlassCard><GlassCard title="Anomaly watch"><AnomalyChart points={anomalies as AnomalyPoint[]} /></GlassCard></div>; }
