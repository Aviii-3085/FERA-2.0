import { Routes, Route, Navigate, useLocation } from "react-router-dom";
import { AppShell } from "./layouts/AppShell";
import { LandingPage } from "./pages/LandingPage";
import { OverviewPage } from "./pages/OverviewPage";
import { PredictionPage } from "./pages/PredictionPage";
import { ModelPage } from "./pages/ModelPage";
import { DatasetPage } from "./pages/DatasetPage";

function WorkspaceRoutes() {
  return (
    <AppShell>
      <Routes>
        <Route path="/overview" element={<OverviewPage />} />
        <Route path="/prediction" element={<PredictionPage />} />
        <Route path="/model" element={<ModelPage />} />
        <Route path="/dataset" element={<DatasetPage />} />
        <Route path="*" element={<Navigate to="/overview" replace />} />
      </Routes>
    </AppShell>
  );
}

function App() {
  const location = useLocation();

  if (location.pathname === "/") {
    return <LandingPage />;
  }

  return <WorkspaceRoutes />;
}

export default App;