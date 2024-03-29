import React from "react";
import { Link } from "react-router-dom";
import styles from "./concert_card.module.css";
import { DateStyled } from "./DateStyled";
export const ConcertCard = ({ props }) => {
  return (
    <Link to={"/concerts/" + props.venue} style={{ textDecoration: "none" }}>
      <div className={styles.concert}>
        <img src={props.photo_url} alt={props.artist_name}></img>
        <div className={styles.concert_info}>
          <DateStyled props={props.date} />
          <div>
            <p>{props.artist_name}</p>
            <p>
              {props.venue} <br></br> {props.location}
            </p>
          </div>
        </div>
      </div>
    </Link>
  );
};
