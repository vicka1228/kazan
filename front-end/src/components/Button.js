import React from "react";
import { Link } from "react-router-dom";
export const Button = (props) => {
  return (
    <Link to={props.link}>
      <button style={{fontSize: '1rem'}}>{props.text}</button>
    </Link>
  );
};
