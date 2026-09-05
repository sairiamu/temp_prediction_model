import type { ForecastPoint } from "../../types";
export function ForecastChart({ points }: { points: ForecastPoint[] }) { return <ul>{points.map((point) => <li key={point.timestamp}>{new Date(point.timestamp).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}: {point.predicted.toFixed(1)}°</li>)}</ul>; }
