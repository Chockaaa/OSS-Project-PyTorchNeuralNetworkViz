import React, { useState } from 'react'
import OutputDisplay from './OutputDisplay'
import axios from 'axios'


function TextBoxForm(){
  
  const [code, setCode] = useState("")
  function handleChange(event){
    setCode(event.target.value)
  }

  const [click, setClick] = useState(false)
  const [output, setOutput] = useState("")
  function handleSubmit(event){
    event.preventDefault()
    setClick(true)
    setOutput(code)
    //put in the fetch function to send the data to a json file
    //TODO: net:Error because the flask-server file is not in this folder directory
    axios.post('http://localhost:5000', {
      // Add parameters here
      mode: "TextEditor",
      body: output,

    })
    .then((response) => {
      console.log(response.data);

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
          output!='' ? <OutputDisplay code = {output} /> 
          : <p style={{textAlign: "center", color: "white"}}>You need to copy and paste your code above</p>
        : ""}
      </div>
    </div>
  )
}


export default TextBoxForm