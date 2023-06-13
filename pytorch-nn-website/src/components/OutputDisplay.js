import React from 'react'
import PropTypes from 'prop-types'
import DisplayImage from './DisplayImage'

function OutputDisplay(){
  return (
    <div>
        <h2 className='output'>Output</h2>
        
        <DisplayImage />
        
    </div>
  )
}

export default OutputDisplay