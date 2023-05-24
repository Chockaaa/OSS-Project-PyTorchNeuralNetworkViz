import React from 'react'
import PropTypes from 'prop-types'

function OutputDisplay({code}){
  return (
    <div>
        <h2 className='output'>Output</h2>
        
        <div className='Output-background'>
          <p>{code}</p>
        </div>
    </div>
  )
}

OutputDisplay.propTypes = {
  code: PropTypes.string.isRequired
}

OutputDisplay.defaultProps = {
  code: ""
}


export default OutputDisplay