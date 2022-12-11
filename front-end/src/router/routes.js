import { LoginPage } from "../pages/LoginPage";
import { MainPage } from "../pages/MainPage";

import React from "react";
import { ConcertPage } from "../pages/ConcertPage";

export const routes = [
  {
    path: "/",
    component: <LoginPage />,
  },
  {
    path: "/home",
    component: <MainPage />,
  },
  { path: "/search", component: <ConcertPage /> },
];
