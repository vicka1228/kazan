import React from "react";
import { FavArtists } from "../components/molecules/FavArtists";
import { Sidebar } from "../components/molecules/Sidebar";
export const MainPage = () => {
  return (
    <>
      <Sidebar />
      <FavArtists />
    </>
  );
};
