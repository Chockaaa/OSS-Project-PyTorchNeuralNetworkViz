import React, { useState } from 'react'
import OutputDisplay from './OutputDisplay'
function TextBoxForm(){
  
  const [code, setCode] = useState("")
  function handleChange(event){
    setCode(event.target.value)
  }
  function handleSubmit(event){
    event.preventDefault()
    console.log(event.target.value)
    setCode("")
  }
  return (
    <div>
    <div className='text-container' onSubmit={handleSubmit}>
        <p style={{color:"white", textAlign:"left"}}>Enter your code here :</p>    
        <div className='textbox'>
            <textarea value={code} onChange={handleChange}></textarea>
        </div>  
        <button className='submit-btn'>Generate</button>
    </div>
    <OutputDisplay />
    </div>
  )
}


export default TextBoxForm