import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useEffect, useState } from 'react';
import axios from 'axios'

import { routes } from "./router/routes";
import React from "react";
function App() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.get('http://127.0.0.1:5000/flask/hello').then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
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
