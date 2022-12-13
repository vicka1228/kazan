import React from "react";

export const Button = (props) => {
  return (
    <a href={props.link}>
      <button style={{fontSize: '1rem'}}>{props.text}</button>
    </a>
  );
};
