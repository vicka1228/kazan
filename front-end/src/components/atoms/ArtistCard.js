import styles from "./artist_card.module.css";
import React from "react";
import { Link } from "react-router-dom";

export const ArtistCard = ({ props }) => {
  return (
    <Link to={"/artists/" + props} style={{ textDecoration: "none" }}>
      <div className={styles.artist}>
        <img src={props.src} alt={props}></img>
        <p>{props.replace(/[^a-zA-Z0-9 ]/g, "")}</p>
      </div>
    </Link>
  );
};
