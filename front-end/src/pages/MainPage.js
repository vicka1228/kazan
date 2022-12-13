import React from "react";
import { ConcertsList } from "../components/molecules/ConcertsList";
import { FavArtists } from "../components/molecules/FavArtists";
import { Sidebar } from "../components/molecules/Sidebar";
import axios from "axios";
import { useEffect } from "react";
export const MainPage = () => {

  useEffect(() => {
    axios
      .post("http://127.0.0.1:5000/go")
      .then((response) => {
        console.log("SUCCESS", response);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  return (
    <>
      <Sidebar />
      <div style={{ width: "100%", marginLeft: "20rem" }}>
        <FavArtists />
        <ConcertsList />
      </div>
    </>
  );
};
