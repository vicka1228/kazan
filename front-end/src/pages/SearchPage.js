import React from "react";
import { Sidebar } from "../components/molecules/Sidebar";
import styles from "./page_style.module.css";
import concerts from "../components/dummy/concerts.json";
import { ConcertCard } from "../components/atoms/ConcertCard";
import conc_styles from "../components/molecules/fav_artists.module.css";
import { useState } from "react";
import axios from "axios";
import { useEffect } from "react";

export const SearchPage = () => {
  const [searchField, setSearchField] = useState("");
  const handleChange = (e) => {
    setSearchField(e.target.value);
  };
  //Search API

  const [getSearchResult, setGetSearchResult] = useState({});

  useEffect(() => {
    let req = {
      "search-string": searchField,
    };
    axios
      .post("http://127.0.0.1:5000/flask/search", req)
      .then((response) => {
        console.log("SUCCESS", response);
        setGetSearchResult(response);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [searchField]);
  return (
    <>
      <Sidebar />
      <div style={{ width: "100%", marginLeft: "20rem" }}>
        <div className={styles.search}>
          <input
            type="text"
            placeholder="What do you want to find?"
            onChange={handleChange}
          />
          <svg viewBox="0 0 1000 1000" title="Search">
            <path
              fill="currentColor"
              d="M408 745a337 337 0 1 0 0-674 337 337 0 0 0 0 674zm239-19a396 396 0 0 1-239 80 398 398 0 1 1 319-159l247 248a56 56 0 0 1 0 79 56 56 0 0 1-79 0L647 726z"
            />
          </svg>
        </div>

        <div className={conc_styles.favs}>
          <div className={conc_styles.top}>
            <h2>Results:</h2>
          </div>
          <div className={conc_styles.artists_container}>
            {concerts.map((value) => (
              <ConcertCard props={value} key={value.key} />
            ))}
          </div>
        </div>
      </div>
    </>
  );
};
