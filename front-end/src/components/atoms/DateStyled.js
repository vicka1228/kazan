import React from "react";
export const DateStyled = ({ props }) => {
    console.log(props)
  return (
    <div style={{ display: "flex", flexDirection: "column", justifyContent: "flex-start", gap: "0rem", alignItems: "center" }}>
      <p style={{ color: "var(--grnClr)" }}>{props.month}</p>
      <p style={{ fontSize: "2rem" }}>{props.day}</p>
    </div>
  );
};
