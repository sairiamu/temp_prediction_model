export function GlassCard({ title, children }: { title: string; children: React.ReactNode }) {
  return <article className="card"><h2>{title}</h2>{children}</article>;
}
