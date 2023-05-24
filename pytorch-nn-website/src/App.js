import './App.css';
import {React,useState} from 'react';
import ToggleSwitch from './components/ToggleSwitch';
import TextBoxForm from './components/CustomiseForm';
import OutputDisplay from './components/OutputDisplay';

function App() {
  return (
    <div className="background">
      <h1 className="header">Neural Network Image Generator</h1>
        <ToggleSwitch />
      </div>
  );
}

export default App;
