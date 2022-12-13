import React from "react";
import { ConcertCard } from "../components/atoms/ConcertCard";
import concerts from "../components/dummy/concerts.json";
import styles from "../components/molecules/fav_artists.module.css";
import { Sidebar } from "../components/molecules/Sidebar";

export const ConcertsPage = () => {
  return (
    <>
      <Sidebar />
      <div style={{ width: "100%", marginLeft: "20rem" }}>
        <div className={styles.favs}>
          <div className={styles.top}>
            <h2>Concerts you might like</h2>
          </div>
          <div className={styles.artists_container}>
            {concerts.map((value) => (
              <ConcertCard props={value} key={value.key} />
            ))}
          </div>
        </div>
      </div>
    </>
  );
};
