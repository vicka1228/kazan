import React from "react";
import { Sidebar } from "../components/molecules/Sidebar";
import styles from "./page_style.module.css";
import { ConcertCard } from "../components/atoms/ConcertCard";
import axios from "axios";
import { useEffect } from "react";
import { useState } from "react";
import { useParams } from "react-router-dom";

import concerts from "../components/dummy/concerts.json";
export const ArtistPage = () => {
  const { id } = useParams();

  //Concerts of Artist API

  const [getConcertsOfArtist, setGetConcertsofArtist] = useState({});
  let artist = id; //have to accept from user
  let req = {
    'artist': artist
  };
  useEffect(() => {
    axios
      .post("http://127.0.0.1:8080/flask/artistconcerts", req)
      .then((response) => {
        console.log("SUCCESS", response);
        setGetConcertsofArtist(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const [getImageOfArtist, setGetImageofArtist] = useState({});
  
  useEffect(() => {
    axios
      .post("http://127.0.0.1:8080/flask/artistimage", req)
      .then((response) => {
        console.log("SUCCESS", response);
        setGetImageofArtist(response);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <>
      <Sidebar />
      <div className={styles.artist_page}>
        <div className={styles.artist_banner}>
          {/* <img src="https://connorgroup.com/static/4bb1b295ecca0123d20cd18be8066649/cd40e/Concerts_near_San_Antonio-scaled.jpg"></img>
          <p>The Weeknd</p> */}
          <img src={getImageOfArtist.imageURL}></img>
          <p>{artist}</p>
        </div>
        <div className={styles.container}>
          <div className={styles.artist_concerts}>
            {getConcertsOfArtist.concerts.map((value) => (
              <ConcertCard props={value} key={value.key} />
            ))}
          </div>
        </div>
      </div>
    </>
  );
};
