import React from "react";
import styles from "./sidebar.module.css";
import home from "../images/home.svg";
import search from "../images/search.svg";
import library from "../images/library.svg";
export const Sidebar = () => {
  const given = 0;
  const nav = [
    { name: "Home", src: home },
    { name: "Search", src: search },
    { name: "Your library", src: library },
  ];
  return (
    <aside className={styles.sidebar}>
      <div>
        <h2>Kazan</h2>
        <ul>
          {nav.map((value, index) => (
            <li key={index} className={given === index ? styles.active : ""}>
              <img src={value.src} alt={value.name} />
              {value.name}
            </li>
          ))}
        </ul>
      </div>
      <p
        style={{
          alignItems: "center",
          display: "flex",
          gap: "0.375rem",
          justifyContent: "center",
        }}
      >
        Connected to
        <img
          height="28"
          alt="Spotify logo"
          src="https://www.edigitalagency.com.au/wp-content/uploads/Spotify_Logo-png-RGB-Green.png"
        ></img>
      </p>
    </aside>
  );
};
