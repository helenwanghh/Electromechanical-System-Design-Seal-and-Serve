import React from 'react';
import './StartPage.css'; // Import your CSS file
//import { BrowserRouter, Route } from 'react-router-dom';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import StartPage from './StartPage';
import CustomPage from './CustomPage';
import PresavedPage from './PresavedPage';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<StartPage />} />
        <Route path="/custom-drink" element={<CustomPage />} />
        <Route path="/presaved-drink" element={<PresavedPage />} />
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

// App.js



