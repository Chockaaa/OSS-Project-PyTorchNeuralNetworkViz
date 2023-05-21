import React from 'react'
import { useState } from 'react';

function CustomiseForm(){
    
    const [layer,setLayer] = useState([{layer:""}])
    console.log(layer);
  
    const[output,setOutput] =useState([]);
  
    const handleLayerAdd=()=>{
      setLayer([...layer,{layer:""}])
    }
  
    const handleLayerRemove=(index) =>{
      const layer_list=[...layer];
      layer_list.splice(index,1);
      setLayer(layer_list);
    }
  
    const handleLayerChange=(e,index)=>{
      const{name,value} = e.target
      const layer_list=[...layer];
      layer_list[index][name] = value;
      setLayer(layer_list);
    }
  
    const handleFormSubmit=(e)=>{
      e.preventDefault();
      const outputData =layer.map((singleLayer)=>singleLayer.layer);
      setOutput(outputData);
    }
    
    return(
    <div>
        <form className="form" >
                
            {layer.map((singleLayer,index)=>(
            <div className='form-group'>
            <div key={index} className='Layers'>

                <label htmlFor="Layer" className='label'>Layer {index+1}
                </label>
                <div>
                
                <label htmlFor="no_neurons" className='no_neurons'>
                    Number of Neurons:  </label>

                <input type='number' name='layer' className='input'
                    value={singleLayer.no_neurons}
                    onChange={(e)=>handleLayerChange(e,index)}
                />
                    
                    {layer.length>1 && 
                    <button type='button' className='remove-btn' onClick={()=>handleLayerRemove(index)}>
                    <span>Remove Layer</span>
                    </button>
                    }
                    
                </div>
                    {layer.length-1 ===index && layer.length<4 && 
                    <button type='button' className='add-btn' onClick={handleLayerAdd}>
                    <span>Add Layer</span>
                    </button>
                    }    
                </div>
            </div>  

            ))}
            
        
            <button type='button' className='submit-btn' onClick={handleFormSubmit}><span>Submit</span></button>

        </form>
        {/* <h2 className='Output'>Output</h2> */}

        {/* <div className="Output-background">
              {output.length>0 && (
                <div className='output-layer'>
                  layers=[{output.join(',')}]
                  </div>
              )}
         </div> */}
    </div> 
)
}

export default CustomiseForm