import React from 'react'
import { useState } from 'react';
import OutputDisplay from './OutputDisplay';
import Dropdown from './Dropdown';

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

    //Generate button click
    const [click, setClick] = useState(false)
    const handleSubmitClick = () =>{
      setClick(true)
      // setTimeout(() => {
      //   setClick(false)},
      //   2000)
      }

    const handleFormSubmit=(e)=>{
      e.preventDefault();
      const outputData =layer.map((singleLayer)=>singleLayer.layer);
      setOutput(outputData);
      handleSubmitClick();
    }
    
    const handleOutput = (array) => {
      let concatString = ""
      array.length > 0 ? concatString = array.join(',') : concatString = ""
      return concatString;
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

                  <div className='dropdown-container'>
                    <label>Select Layer Type</label>
                    <Dropdown options={[
                      {value:'ReLu', label: 'ReLu'},
                      {value: 'Convo2d', label: 'Convo2d'},
                      {value: 'pool2d', label: 'pool2d'}]}/>
                  </div>

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
            <button type='button' className='submit-btn' onClick={handleFormSubmit}>
                <span>Generate</span>
            </button>
           
            <div className='Output-container'>
            {click ? 
              (output['0']!='' ? <OutputDisplay code={'Layers = '+ handleOutput(output)}/> 
              : <p style={{textAlign: "center", color: "white"}}>You need to select the number of layers</p>) 
              : ""}
            </div>

        </form>
        
         
    </div> 
)
}

export default CustomiseForm