import styles from "./artist_card.module.css";
import React from "react";

export const ArtistCard = ({ props }) => {
  return (
    <div className={styles.artist}>
      <img src={props.src} alt={props.name}></img>
      <p>{props.name}</p>
    </div>
  );
};
