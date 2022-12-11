import React from "react";
import { Sidebar } from "../components/molecules/Sidebar";
import styles from "./page_style.module.css";

export const ConcertPage = ({ props }) => {
  return (
    <>
      <Sidebar />
      <div className={styles.concert_page}>
        <img src="https://connorgroup.com/static/4bb1b295ecca0123d20cd18be8066649/cd40e/Concerts_near_San_Antonio-scaled.jpg"></img>
      </div>
    </>
  );
};
