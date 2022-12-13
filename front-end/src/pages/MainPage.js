import React from "react";
import { ConcertsList } from "../components/molecules/ConcertsList";
import { FavArtists } from "../components/molecules/FavArtists";
import { Sidebar } from "../components/molecules/Sidebar";
import axios from "axios";
import { useEffect } from "react";
import { useCookies } from "react-cookie";
import { useNavigate } from "react-router-dom";

export const MainPage = () => {
  const [cookies, setCookie] = useCookies();
  const navigate = useNavigate();
  const data = {
    token: cookies.token,
    expires_at: parseInt(cookies.expires_at),
    refresh_token: cookies.refresh_token,
  };
  useEffect(() => {
    axios
      .post("http://127.0.0.1:8080/go", data)
      .then((response) => {
        console.log("SUCCESS", response.data);
        return response.data;
      })
      .then((data) => {
        if (data["redirect"]) {
          navigate("/");
        }
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  return (
    <>
      <Sidebar />
      <div style={{ width: "100%", marginLeft: "20rem" }}>
        <FavArtists />
        <ConcertsList />
      </div>
    </>
  );
};
