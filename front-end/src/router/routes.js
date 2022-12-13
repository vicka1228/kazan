import { LoginPage } from "../pages/LoginPage";
import { MainPage } from "../pages/MainPage";

import React from "react";
import { ConcertPage } from "../pages/ConcertPage";
import { ArtistsPage } from "../pages/ArtistsPage";
import { ArtistPage } from "../pages/ArtistPage";
import { ConcertsPage } from "../pages/ConcertsPage";
import { SearchPage } from "../pages/SearchPage";

export const routes = [
  {
    path: "/",
    component: <LoginPage />,
  },
  {
    path: "/home",
    component: <MainPage />,
  },
  { path: "/search", component: <SearchPage /> },
  { path: "/concerts", component: <ConcertsPage /> },
  { path: "/concerts/:id", component: <ConcertPage /> },
  { path: "/artists", component: <ArtistsPage /> },
  { path: "/artists/:id", component: <ArtistPage /> },
];
