# .\venv\Scripts\activate

from flask import Flask, jsonify, send_file,request

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return {'test': 'test'}


# @app.route('/generate_image', methods=['POST'])
# def generate_image():
#     data = request.get_json()
#     parameter1 = data['parameter1']
#     parameter2 = data['parameter2']

#     text = "This is the generated image"
#     image_path = '../helloworld.png'
#     response = {
#         'file': send_file(image_path, mimetype='image/png'),
#         'text': text
#     }
    
    
#     return jsonify(response)

@app.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.get_json()
    parameter1 = data['parameter1']
    parameter2 = data['parameter2']

    text = "This is the generated image"
    image_path = '../helloworld.png'
    
    
    
    return send_file(image_path, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)