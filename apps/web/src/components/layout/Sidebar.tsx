import type { PageKey } from "../../types";

const items: Array<[PageKey, string]> = [
  ["dashboard", "Dashboard"],
  ["upload", "Upload data"],
  ["forecast", "Forecast"],
  ["anomalies", "Anomalies"],
  ["classification", "Classification"],
];

export function Sidebar({ activePage, onNavigate }: { activePage: PageKey; onNavigate: (page: PageKey) => void }) {
  return <aside className="sidebar"><h1 className="brand">Temp Prediction</h1><nav className="nav" aria-label="Main navigation">{items.map(([key, label]) => <button className={`nav-button ${activePage === key ? "active" : ""}`} key={key} onClick={() => onNavigate(key)}>{label}</button>)}</nav></aside>;
}
