import artists from "../dummy/artists.json";
import React from "react";
import { ArtistCard } from "../atoms/ArtistCard";
import styles from "./fav_artists.module.css";

export const FavArtists = () => {
  return (
    <div className={styles.favs}>
      <div className={styles.top}>
        <h2>Favorite artists</h2>
        <p>SEE ALL</p>
      </div>
      <div className={styles.artists_container}>
        {artists.slice(0, 6).map((value) => (
          <ArtistCard props={value} key={value.key} />
        ))}
      </div>
    </div>
  );
};
