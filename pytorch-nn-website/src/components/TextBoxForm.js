import React, { useState } from 'react'
import OutputDisplay from './OutputDisplay'
import axios from 'axios'

function TextBoxForm(){
  
  const [code, setCode] = useState("")
  function handleChange(event){
    setCode(event.target.value)
  }

  const [click, setClick] = useState(false)
  function handleSubmit(event){
    event.preventDefault()
    setClick(true)
    setCode(code)
    console.log(code)
    axios.post('http://127.0.0.1:5000/generate_image', {
      "modelInputversion": 1,
      "architecture": code,
      // "architecture": "NeuralNetwork(\n  (flatten): Flatten(start_dim=1, end_dim=-1)\n  (linear_relu_stack): Sequential(\n    (0): Linear(in_features=64, out_features=64, bias=True)\n    (1): ReLU()\n    (2): Linear(in_features=16, out_features=16, bias=True)\n    (3): Tanh()\n    (4): Linear(in_features=8, out_features=2, bias=True)\n  )\n)",
      "view": "right"
    }, {
      headers: {
        "Content-Type": "application/json"
      }
    })
    .then((response) => {
      console.log(response.data)
    })
    .catch((error) => {
      console.log(error);
    })
  }

  return (
    <div>
      <div className='text-container'>
          <p style={{color:"white", textAlign:"left"}}>Paste your code here :</p>    
          <div className='textbox'>
              <textarea value={code} onChange={handleChange} 
              placeholder='e.g. model = nn.Sequential(nn.Conv2d(1,20,5), nn.ReLU(), nn.Conv2d(20,64,5), nn.ReLU())'>
              </textarea>
          </div>  
          <button className='submit-btn' onClick={handleSubmit}>Generate</button>
      </div>
      <div className='Output-container'>
        {click ? 
          code!=='' ? <OutputDisplay /> 
          : <p style={{textAlign: "center", color: "white"}}>You need to copy and paste your code above</p>
        : ""}
      </div>
    </div>
  )
}


export default TextBoxForm