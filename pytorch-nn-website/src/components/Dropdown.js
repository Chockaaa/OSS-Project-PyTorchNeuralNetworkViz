import React, { useState } from 'react'
import PropTypes from 'prop-types'

function Dropdown({options, selectOption}){
   const selectLayer = (e) => {
    let idx = e.target.selectedIndex;
    selectOption(options[idx].value);
    }

   return (
    <div>
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