# .\venv\Scripts\activate

import ast
import io
from flask import Flask, jsonify, send_file,request
from ImageGeneratorSupportCode import *
from backend_image_generator import NeuralNetworkGenerator

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return {'test': 'test'}

@app.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.get_json()
    modelInputversion = data['modelInputversion']
    

    if modelInputversion == 1:
        architecture = data['architecture']
        ImageViewingAngle = data['view']
        layer_info = extract_layer_info(architecture)
        is_linear_activation = is_linear_activation_network(layer_info)
        if(is_linear_activation):
            layer_names, num_neurons = process_layer_info(layer_info)
            print(ImageViewingAngle)
            print(layer_names)
            print(num_neurons)
        else:
            print("Not a linear activation network")
    if modelInputversion == 2:
       
        layer_names = ast.literal_eval(data['architecture'])
        num_neurons = ast.literal_eval(data['neurons'])
        ImageViewingAngle = data['view']

    # GenerateImage Function
    generator = NeuralNetworkGenerator()
    image_path = generator.generate_neural_network(layer_names, num_neurons, ImageViewingAngle)

    if image_path is None:
        # Handle error condition
        return {'error': 'Unable to generate the neural network image.'}
    # End of Image Generation function


     # Convert the image to a byte stream
    image_bytes = io.BytesIO()
    with open(image_path, 'rb') as image_file:
        image_bytes.write(image_file.read())

    # Send the image file as a response
    image_bytes.seek(0)
    return send_file(image_bytes, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
