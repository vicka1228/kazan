import React from "react";
import { ConcertsList } from "../components/molecules/ConcertsList";
import { FavArtists } from "../components/molecules/FavArtists";
import { Sidebar } from "../components/molecules/Sidebar";
export const MainPage = () => {
  return (
    <>
      <Sidebar />
      <div style={{width: "100%", marginLeft: "20rem"}}>
        <FavArtists />
        <ConcertsList />
      </div>
    </>
  );
};
