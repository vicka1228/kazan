import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useEffect, useState } from 'react';
import axios from 'axios'

import { routes } from "./router/routes";
import React from "react";
function App() {

  //test API
  const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.get('http://127.0.0.1:5000/flask/hello').then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])

  //Concerts List API

  const [getConcertsList, setGetConcertsList] = useState({})

  useEffect(()=>{
    axios.get('http://127.0.0.1:5000/flask/concerts').then(response => {
      console.log("SUCCESS", response)
      setGetConcertsList(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])

  //Artists List API

  const [getArtistsList, setGetArtistsList] = useState({})

  useEffect(()=>{
    axios.get('http://127.0.0.1:5000/flask/artists').then(response => {
      console.log("SUCCESS", response)
      setGetArtistsList(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])

  //Concert Info API

  const [getConcertInfo, setGetConcertInfo] = useState({})
  venue = "" //have to accept from user
  req = {
    'venue': venue
  }
  useEffect(()=>{
    axios.post('http://127.0.0.1:5000/flask/concertinfo', req).then(response => {
      console.log("SUCCESS", response)
      setGetConcertInfo(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])

  //Search API

  const [getSearchResult, setGetSearchResult] = useState({})
  searchString = "" //have to accept from user
  req = {
    'search-string': searchString
  }
  useEffect(()=>{
    axios.post('http://127.0.0.1:5000/flask/search', req).then(response => {
      console.log("SUCCESS", response)
      setGetSearchResult(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])


  //Concerts of Artist API

  const [getConcertsOfArtist, setGetConcertsofArtist] = useState({})
  artist = "" //have to accept from user
  req = {
    'artist': artist
  }
  useEffect(()=>{
    axios.post('http://127.0.0.1:5000/flask/artistconcerts', req).then(response => {
      console.log("SUCCESS", response)
      setGetConcertsofArtist(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])




  return (
    
    <div className="App">
    <div>{getMessage.status === 200 ? 
      <h3>{getMessage.data.message}</h3>
      :
      <h3>LOADING</h3>}</div>
      <BrowserRouter>
      <Routes>
        {routes.map((route, i) => (
          <Route key={i} path={route.path} element={route.component} />
        ))}
      </Routes>
    </BrowserRouter>
      </div>
  );
}

export default App;
