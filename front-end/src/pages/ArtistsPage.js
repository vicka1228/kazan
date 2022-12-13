import artists from "../components/dummy/artists.json";
import React from "react";
import { ArtistCard } from "../components/atoms/ArtistCard";
import styles from "../components/molecules/fav_artists.module.css";
import axios from "axios";
import { useEffect, useState } from "react";
import { Sidebar } from "../components/molecules/Sidebar";

export const ArtistsPage = () => {
  //Artists List API

  const [getArtistsList, setGetArtistsList] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8080/flask/artists")
      .then((response) => {
        console.log("SUCCESS", response);
        setGetArtistsList(response.data["artists"].split(","));
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  // console.log(getArtistsList);
  return (
    <>
      <Sidebar />
      <div style={{ width: "100%", marginLeft: "20rem" }}>
        <div className={styles.favs}>
          <div className={styles.top}>
            <h2>Favorite artists</h2>
          </div>
          <div className={styles.artists_container}>
            {getArtistsList
              ? getArtistsList.map((value, index) => (
                  <ArtistCard props={value} key={index} />
                ))
              : artists.map((value) => (
                  <ArtistCard props={value} key={value.key} />
                ))}
          </div>
        </div>
      </div>
    </>
  );
};
