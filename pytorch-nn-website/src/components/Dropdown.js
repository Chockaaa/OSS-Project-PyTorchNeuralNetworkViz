import React, { useState } from 'react'
import PropTypes from 'prop-types'

function Dropdown({options}){
    /*options: an array of options for the dropdown*/
   const [layer, setLayer] = useState("")
   const selectLayer = (e) => {
    let idx = e.target.selectedIndex;
    setLayer(e.target.options[idx].value);
    }

   return (
    <div>
        {/* <div className='dropdown-bar' onClick={handleClick}> */}
            {/* <div>
                <p style={{fontSize:15,paddingLeft:10}}>Select...</p>
            </div>
        </div> */}
          <select className='dropdown-menu' onChange={selectLayer}>
            {options.map((option)=>(
                <option key={option.value} className='dropdown-item'>
                  {option.label}
                </option>
            ))}
          </select>
    </div>
  )
}

Dropdown.propTypes = {}

export default Dropdown