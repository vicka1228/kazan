import React from "react";
import { ConcertCard } from "../atoms/ConcertCard";
import concerts from "../dummy/concerts.json";
import styles from "./fav_artists.module.css";

export const ConcertsList = () => {
  return (
    <div className={styles.favs}>
      <div className={styles.top}>
        <h2>Concerts you might like</h2>
        <p>SEE ALL</p>
      </div>
      <div className={styles.artists_container}>
        {concerts.map((value) => (
          <ConcertCard props={value} key={value.key} />
        ))}
      </div>
    </div>
  );
};
