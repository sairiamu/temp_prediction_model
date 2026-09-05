import type { PageKey } from "../../types";

export function Header({ page }: { page: PageKey }) {
  const label = page[0].toUpperCase() + page.slice(1);
  return <header className="header"><div><p className="eyebrow">Monitoring workspace</p><h2 className="title">{label}</h2></div><span className="muted">Mock mode</span></header>;
}
