import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import './style/App.css'
import UrlShortener from "./urlshortener";
import { BrowserRouter, Route, Routes} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<UrlShortener/>} />
      </Routes>    
    </BrowserRouter> 
  );
}

export default App
