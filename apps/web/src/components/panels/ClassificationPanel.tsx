import type { ClassificationResult } from "../../types";
export function ClassificationPanel({ result }: { result: ClassificationResult }) { return <div className="card"><h2>{result.regime}</h2><p>Confidence: {Math.round(result.confidence * 100)}%</p>{result.signals.map((signal) => <p className="muted" key={signal}>{signal}</p>)}</div>; }
