import React from 'react'
import { useState } from 'react'
import CustomiseForm from './CustomiseForm'
import TextBoxForm from './TextBoxForm'

function ToggleSwitch(){
    let [toggle, setToggle] = useState(true)
    const handleToggle = () => {
        setToggle(!toggle)
    }

    return (
        <div>
            <div className='container' onClick={handleToggle}>        
                <h4 className = "switch-options">{toggle ? "Text Editor" : "Customise"}</h4>
            </div>
            {toggle ? (
                <div>
                    <TextBoxForm />
                </div>
            ) : (
                <div>
                    <CustomiseForm />
                </div>
            )}
        </div>
  )
}

export default ToggleSwitch