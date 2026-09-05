export function SkeuoGauge({ value }: { value: number }) {
  return <div className="metric" aria-label={`${Math.round(value * 100)} percent`}>{Math.round(value * 100)}%</div>;
}
