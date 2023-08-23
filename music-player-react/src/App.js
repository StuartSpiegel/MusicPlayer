import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Music Player</h1>
      <audio controls>
        <source src="/play" type="audio/mpeg" />
        Your browser does not support the audio element.
      </audio>
    </div>
  );
}

export default App;
