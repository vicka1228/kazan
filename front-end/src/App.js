import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
// import { useEffect, useState } from "react";
// import axios from "axios";

import { routes } from "./router/routes";
import React from "react";
function App() {
  //test API
  // const [getMessage, setGetMessage] = useState({});

  // useEffect(() => {
  //   axios
  //     .get("http://127.0.0.1:5000/flask/hello")
  //     .then((response) => {
  //       console.log("SUCCESS", response);
  //       setGetMessage(response);
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // }, []);

  // //Concerts List API

  // const [getConcertsList, setGetConcertsList] = useState({});

  // useEffect(() => {
  //   axios
  //     .get("http://127.0.0.1:5000/flask/concerts")
  //     .then((response) => {
  //       console.log("SUCCESS", response);
  //       setGetConcertsList(response);
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // }, []);

  // //Artists List API

  // const [getArtistsList, setGetArtistsList] = useState({});

  // useEffect(() => {
  //   axios
  //     .get("http://127.0.0.1:5000/flask/artists")
  //     .then((response) => {
  //       console.log("SUCCESS", response);
  //       setGetArtistsList(response);
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // }, []);

  // //Concert Info API

  // const [getConcertInfo, setGetConcertInfo] = useState({});
  // let id = ""; //have to accept from user
  // let req = {
  //   'id': id
  // };
  // useEffect(() => {
  //   axios
  //     .post("http://127.0.0.1:5000/flask/concertinfo", req)
  //     .then((response) => {
  //       console.log("SUCCESS", response);
  //       setGetConcertInfo(response);
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // }, []);

  // //Search API

  // const [getSearchResult, setGetSearchResult] = useState({});
  // let searchString = ""; //have to accept from user
  // req = {
  //   "search-string": searchString
  // };
  // useEffect(() => {
  //   axios
  //     .post("http://127.0.0.1:5000/flask/search", req)
  //     .then((response) => {
  //       console.log("SUCCESS", response);
  //       setGetSearchResult(response);
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // }, []);

  // //Concerts of Artist API

  // const [getConcertsOfArtist, setGetConcertsofArtist] = useState({});
  // let artist = ""; //have to accept from user
  // req = {
  //   'artist': artist
  // };
  // useEffect(() => {
  //   axios
  //     .post("http://127.0.0.1:5000/flask/artistconcerts", req)
  //     .then((response) => {
  //       console.log("SUCCESS", response);
  //       setGetConcertsofArtist(response);
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // }, []);

  // //Image of Artist API

  // const [getImageOfArtist, setGetImageofArtist] = useState({});
  // let artist = ""; //have to accept from user
  // req = {
  //   'artist': artist
  // };
  // useEffect(() => {
  //   axios
  //     .post("http://127.0.0.1:5000/flask/artistimage", req)
  //     .then((response) => {
  //       console.log("SUCCESS", response);
  //       setGetImageofArtist(response);
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // }, []);

  // //Image of Concert API

  // const [getImageOfConcert, setGetImageofConcert] = useState({});
  // let id = ""; //have to accept from user
  // req = {
  //   'id': id
  // };
  // useEffect(() => {
  //   axios
  //     .post("http://127.0.0.1:5000/flask/concertimage", req)
  //     .then((response) => {
  //       console.log("SUCCESS", response);
  //       setGetImageofConcert(response);
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // }, []);

  return (
      <BrowserRouter>
        <Routes>
          {routes.map((route, i) => (
            <Route key={i} path={route.path} element={route.component} />
          ))}
        </Routes>
      </BrowserRouter>

  );
}

export default App;
