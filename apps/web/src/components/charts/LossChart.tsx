import type { LossPoint } from "../../types";
export function LossChart({ points }: { points: LossPoint[] }) { return <p className="muted">{points.length} training epochs loaded. Latest validation loss: {points.at(-1)?.validation.toFixed(2)}</p>; }
