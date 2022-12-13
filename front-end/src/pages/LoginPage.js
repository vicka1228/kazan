import { Button } from "../components/atoms/Button";
import { Divider } from "../components/atoms/Divider";
import React from "react";

export const LoginPage = () => {
  return (
    <>
      <div
        style={{
          width: "100%",
          height: "100vh",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          gap: "1.5rem",
          position: "relative",
        }}
      >
        <h1>Kazan</h1>
        <p
          style={{
            alignItems: "center",
            display: "flex",
            gap: "0.375rem",
          }}
        >
          Connected to
          <img
            height="28"
            alt="Spotify logo"
            src="https://www.edigitalagency.com.au/wp-content/uploads/Spotify_Logo-png-RGB-Green.png"
          ></img>
        </p>
        <Divider />
        <Button
          text={"Login with Spotify"}
          link={"http://127.0.0.1:5000/login"}
        />
        <div
          style={{
            position: "absolute",
            bottom: "10%",
            width: "20rem",
            height: "auto",
          }}
        >
          <Divider />
          <p
            style={{
              fontSize: "0.75rem",
            }}
            align="center"
          >
            This app connects to Spotify API via OAuth 2.0. Your top artists
            list is one of the data you can access once authenticated.
          </p>
        </div>
      </div>
    </>
  );
};
