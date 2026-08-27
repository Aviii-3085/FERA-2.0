import { Routes, Route, Navigate } from "react-router-dom";
import { AppShell } from "./layouts/AppShell";
import { OverviewPage } from "./pages/OverviewPage";
import { PredictionPage } from "./pages/PredictionPage";
import { ModelPage } from "./pages/ModelPage";
import { DatasetPage } from "./pages/DatasetPage";

function App() {
  return (
    <AppShell>
      <Routes>
        <Route path="/" element={<Navigate to="/overview" replace />} />
        <Route path="/overview" element={<OverviewPage />} />
        <Route path="/prediction" element={<PredictionPage />} />
        <Route path="/model" element={<ModelPage />} />
        <Route path="/dataset" element={<DatasetPage />} />
        <Route path="*" element={<Navigate to="/overview" replace />} />
      </Routes>
    </AppShell>
  );
}

export default App;
