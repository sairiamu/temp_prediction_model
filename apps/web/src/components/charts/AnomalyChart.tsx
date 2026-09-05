import type { AnomalyPoint } from "../../types";
export function AnomalyChart({ points }: { points: AnomalyPoint[] }) { return <p>{points.filter((point) => point.isAnomaly).length} anomaly detected in the latest sample window.</p>; }
