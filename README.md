# Neural Network Image Generator Web Tool
![PyTorch Vizualization Tool](https://github.com/Chockaaa/OSS-Project-PyTorchNeuralNetworkViz/assets/29830837/f8070edb-b1a1-4cc5-b210-ae9edd906ac6)

This is a web tool that combines Flask for backend development and React for frontend implementation to provide customizable 3D visualizations of neural network architectures based on user inputs.

## Testing Backend Server
<p align="center">
  <img src="https://github.com/Chockaaa/OSS-Project-PyTorchNeuralNetworkViz/assets/29830837/b9861958-252d-4c0a-8126-13c7a5ab7f25" width="640">
</p>


## Frontend UI

<p> Users can toggle between "Text Editor" and "Customisation" modes to generate the image </p>

### Text Editor Mode
<p align="center">
  <img src="images/homepage.png" width="640">
  <p>Users can simply copy and paste their pytorch neural network code into the textbox</p>
</p>

### Customisation Mode
<p align ="center">
    <img src="images/customiseLayers.png" width="640">
    <p>Users can select and customise the layers they want from scratch here as well</p>
    <p>For this project, we limited to only 2 types of layers: Linear and Activation Functions (ReLU, Sigmoid, Tanh, LeakyReLU, Softmax) </p>
</p>

### Output 
<p align ="center">
    <img src="images/outputpage.png" width="640">
    <p>Upon pressing the "Generate" button, the neural network image will be displayed at the bottom of the page for users</p>
</p>