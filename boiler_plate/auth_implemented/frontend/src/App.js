import React from 'react';
import {BrowserRouter, Route} from 'react-router-dom'
import NavBar from './components/NavBar'
import Router from './Router'


function App() {
  return (
    <BrowserRouter>
      <NavBar />
      <div className='container mt-3'>
        <div className='row'>
          <div className='col-md-10 offset-md-1 col-xs-12'>
            <Router />
          </div>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
