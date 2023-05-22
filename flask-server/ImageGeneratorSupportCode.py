import re

def extract_layer_info(text):
    layer_info = []
    pattern = r"\((\d+)\):\s*(\w+)\((.*)\)"
    matches = re.findall(pattern, text)
    
    for match in matches:
        layer_number = int(match[0])
        layer_type = match[1]
        layer_params = match[2].split(',')
        
        layer_info.append({
            "layer_number": layer_number,
            "layer_type": layer_type,
            "layer_params": layer_params
        })
    
    return layer_info

def is_linear_activation_network(layer_info):
    activation_functions = ['ReLU', 'LeakyReLU', 'Sigmoid', 'Tanh', 'Softmax']
    
    for layer in layer_info:
        layer_type = layer['layer_type']
        if layer_type != 'Linear' and layer_type not in activation_functions:
            return False
    return True

def process_layer_info(layer_info):
    layer_names = []
    num_neurons = []
    
    for layer in layer_info:
        layer_type = layer['layer_type']
        if layer_type == 'Linear':
            layer_names.append(layer_type)
            params = layer['layer_params']
            num_neurons.append(int(params[1].split('=')[1].strip()))
        else:
            layer_names.append(layer_type)
            num_neurons.append(0)
    
    return layer_names, num_neurons