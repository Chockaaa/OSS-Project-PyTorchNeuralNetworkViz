import React from 'react'
import { useState } from 'react';
import OutputDisplay from './OutputDisplay';
import Dropdown from './Dropdown';

function CustomiseForm(){
    
    const [layer,setLayer] = useState([{number_neurons:0, activation_function:"ReLU" }])
    const[neuronLayer,setNeuronLayer] =useState([]);
    const[functionLayer,setFunctionLayer] =useState([]);


    console.log(layer);
  
    const handleLayerAdd=()=>{
      setLayer([...layer,{number_neurons:0, activation_function:"ReLU"}])
    }
  
    const handleLayerRemove=(index) =>{
      const layer_list=[...layer];
      layer_list.splice(index,1);
      setLayer(layer_list);
    }
  
    const handleLayerChange=(e,index)=>{
      const{name,value} = e.target
      console.log(e)
      console.log(name,value)
      const layer_list=[...layer];
      layer_list[index][name] = value;
      setLayer(layer_list);
    }

    const handleSelectOption=(value,index)=>{
      const layer_list=[...layer];
      layer_list[index]['activation_function'] = value;
      setLayer(layer_list);
    }

    //Generate button click
    const [click, setClick] = useState(false)
    const handleSubmitClick = () =>{
      setClick(true)
      }
    const handleFormSubmit=(e)=>{
      e.preventDefault();
      const outputNeuronsData =layer.map((singleLayer)=>singleLayer.number_neurons);
      setNeuronLayer(outputNeuronsData);

      const outputFunctionData =layer.map((singleLayer)=>singleLayer.activation_function);
      setFunctionLayer(outputFunctionData);
      handleSubmitClick();
    }
    
    const handleOutput = (array) => {
      console.log(array)
      let concatString = "[";
    
      if (array.length > 0) {
        concatString += array.join(',');
      }
    
      concatString += "]";
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
                      {value:'ReLU', label: 'ReLU'},
                      {value: 'Sigmoid', label: 'Sigmoid'},
                      {value: 'Tanh', label: 'Tanh'},
                      {value: "LeakyReLU", label: "LeakyReLU"},
                      {value: "Softmax", label: "Softmax"},
                      {value: "Linear", label: "Linear"}
                      ]} selectOption={(e)=>handleSelectOption(e,index)}
                      />
                  </div>

                  <label htmlFor="no_neurons" className='no_neurons'>
                      Number of Neurons:  </label>
                  
                  {layer['0']["activation_function"] == 'Linear' ? 
                  <input type='number' min="0" step="1" name='number_neurons' className='input'
                      value={singleLayer.number_neurons}
                      onChange={(value)=>handleLayerChange(value,index)}
                  /> : 
                  <input type='number' value="0" name='number_neurons' className='input'/>
                  }
                    
                    {layer.length>1 && 
                    <button type='button' className='remove-btn' onClick={()=>handleLayerRemove(index)}>
                    <span>Remove Layer</span>
                    </button>
                    }      
                    
                </div>
                    {layer.length-1 ===index && layer.length<8 && 
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
              <OutputDisplay code={
                <div> 
                  {'Layers = ' + handleOutput(functionLayer)}
                  <br />
                  {'Neurons = ' +  handleOutput(neuronLayer)}
                </div>
              }/> : ""}
            </div>

        </form>
        
         
    </div> 
)
}

export default CustomiseForm