export function ClayButton({ children, onClick }: { children: React.ReactNode; onClick?: () => void }) {
  return <button className="nav-button active" onClick={onClick}>{children}</button>;
}
