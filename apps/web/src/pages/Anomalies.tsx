import anomalies from "../mocks/mockAnomalies.json";
import { AnomalyChart } from "../components/charts/AnomalyChart";
import type { AnomalyPoint } from "../types";
export function Anomalies() { return <div className="card"><h2>Residual and isolation forest detectors</h2><AnomalyChart points={anomalies as AnomalyPoint[]} /></div>; }
