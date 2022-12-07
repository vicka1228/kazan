import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { routes } from "./router/routes";
import React from "react";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        {routes.map((route, i) => (
          <Route key={i} path={route.path} element={route.component} />
        ))}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
