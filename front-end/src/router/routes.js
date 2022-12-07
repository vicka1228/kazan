import { LoginPage } from "../pages/LoginPage";
import { MainPage } from "../pages/MainPage";
import React from "react";

export const routes = [
  {
    path: "/",
    component: <LoginPage />,
  },
  {
    path: "/home",
    component: <MainPage />,
  },
];
