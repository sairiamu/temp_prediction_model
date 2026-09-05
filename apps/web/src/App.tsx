import { useState } from "react";
import { Header } from "./components/layout/Header";
import { Sidebar } from "./components/layout/Sidebar";
import { Dashboard } from "./pages/Dashboard";
import { Anomalies } from "./pages/Anomalies";
import { Classification } from "./pages/Classification";
import { Forecast } from "./pages/Forecast";
import { Upload } from "./pages/Upload";
import type { PageKey } from "./types";

export default function App() {
  const [page, setPage] = useState<PageKey>("dashboard");
  const content = {
    dashboard: <Dashboard />,
    upload: <Upload />,
    forecast: <Forecast />,
    anomalies: <Anomalies />,
    classification: <Classification />,
  }[page];

  return (
    <div className="app-shell">
      <Sidebar activePage={page} onNavigate={setPage} />
      <main className="main-content">
        <Header page={page} />
        {content}
      </main>
    </div>
  );
}
