import React from "react";
import { Sidebar } from "../components/molecules/Sidebar";
import styles from "./page_style.module.css";

export const SearchPage = () => {
  return (
    <>
      <Sidebar />
      <div style={{ width: "100%", marginLeft: "20rem" }}>
        <div className={styles.search}>
          <input type="text" placeholder="What do you want to find?" />
          <svg viewBox="0 0 1000 1000" title="Search">
            <path
              fill="currentColor"
              d="M408 745a337 337 0 1 0 0-674 337 337 0 0 0 0 674zm239-19a396 396 0 0 1-239 80 398 398 0 1 1 319-159l247 248a56 56 0 0 1 0 79 56 56 0 0 1-79 0L647 726z"
            />
          </svg>
        </div>
      </div>
    </>
  );
};
