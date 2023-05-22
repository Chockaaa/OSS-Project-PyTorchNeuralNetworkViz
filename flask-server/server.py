# .\venv\Scripts\activate

from flask import Flask, jsonify, send_file,request
from ImageGeneratorSupportCode import *
from backend_image_generator import *

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return {'test': 'test'}

@app.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.get_json()
    modelInputversion = data['modelInputversion']
    architecture = data['architecture']
    ImageViewingAngle = data['view']

    if modelInputversion == 1:
        layer_info = extract_layer_info(architecture)
        is_linear_activation = is_linear_activation_network(layer_info)
        if(is_linear_activation):
            layer_names, num_neurons = process_layer_info(layer_info)
            print(ImageViewingAngle)
            print(layer_names)
            print(num_neurons)
        else:
            print("Not a linear activation network")


    # GenerateImage Function
    print(ImageViewingAngle)
    print(layer_names)
    print(num_neurons)

    # End of Image Generation function
        

    image_path = '../helloworld.png'
    return send_file(image_path, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)