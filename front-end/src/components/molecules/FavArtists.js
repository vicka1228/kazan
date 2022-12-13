import artists from "../dummy/artists.json";
import React from "react";
import { ArtistCard } from "../atoms/ArtistCard";
import styles from "./fav_artists.module.css";
import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export const FavArtists = () => {
  //Artists List API

  // const [getArtistsList, setGetArtistsList] = useState([]);

  // useEffect(() => {
  //   axios
  //     .get("http://127.0.0.1:8080/flask/artists")
  //     .then((response) => {
  //       console.log("SUCCESS", response);
  //       setGetArtistsList(response.data["artists"].split(","));
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // }, []);
  // console.log(getArtistsList);
  return (
    <div className={styles.favs}>
      <div className={styles.top}>
        <h2>Favorite artists</h2>
        <Link to="/artists"><p>SEE ALL</p></Link>
      </div>
      <div className={styles.artists_container}>
        {
        // getArtistsList
        //   ? getArtistsList
        //       .slice(0, 6)
        //       .map((value, index) => <ArtistCard props={value} key={index} />)
        //   : 
          artists
              .slice(0, 6)
              .map((value) => <ArtistCard props={value} key={value.key} />)}
      </div>
    </div>
  );
};
