from flask import Flask, send_file
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend


class NeuralNetworkGenerator:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/generate_neural_network', 'generate_neural_network', self.generate_neural_network_route)
        # Define colors for each layer type
        self.layer_colors = {
            'Linear': 'blue',
            'ReLU': 'red',
            'LeakyReLU': 'green',
            'Sigmoid': 'purple',
            'Tanh': 'orange',
            'Softmax': 'yellow'}
        self.used_colors = set()
        self.available_colors = [
            'magenta', 'cyan', 'darkviolet', 'darkgreen', 'darkorange', 'gold', 'hotpink', 'saddlebrown', 'springgreen', 'coral'
        ]

    def generate_neural_network_route(self):
        # Generate the neural network image
        image_path = self.generate_neural_network(layer_names, num_neurons, ImageViewingAngle)

        # Send the image file to the frontend
        return send_file(image_path, mimetype='image/png')

    def generate_neural_network(self, layer_names, num_neurons, ImageViewingAngle):
        # Calculate the offset for centering the circles within each layer
        offsets = [nodes / 2 - 0.5 for nodes in num_neurons]

        # Create a figure and a 3D subplot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the nodes
        x_positions = []
        y_positions = []
        z_positions = []

        for layer, nodes in enumerate(num_neurons):
            if nodes > 0:
                x_positions.extend([layer] * nodes)
                y_positions.extend(range(nodes))
                z_positions.extend([0] * nodes)  # Set z-coordinate to 0 for all nodes

                # Apply the offset to center the circles within each layer
                y_positions[-nodes:] = np.array(y_positions[-nodes:]) - offsets[layer]

        # Color the nodes based on the layer type and coloring rules
        node_colors = []
        activated_linear_layer = False  # Flag to track if the code has been executed

        for i, layer_type in enumerate(layer_names):
            nodes = num_neurons[i]

            if nodes > 0:
                if layer_type != 'Linear':
                    # Assign the color based on the corresponding activation layer from self.layer_colors
                    node_colors.extend([self.layer_colors.get(layer_type, 'black')] * nodes)
                elif layer_type == 'Linear':
                    if i < len(layer_names) - 1 and layer_names[i + 1] == 'Linear':
                        # If the next layer is also a linear layer, color the nodes in the current linear layer as black
                        node_colors.extend(['black'] * nodes)
                    elif i == len(layer_names) - 1 and layer_names[i - 1] == 'Linear':
                        # If the current linear layer is the last layer, color its nodes as black
                        node_colors.extend(['black'] * nodes)
                    else:
                        if activated_linear_layer == False:
                            # If the current layer is the first linear layer following an activation layer
                            activated_linear_layer = True  # Set the flag
                            node_colors.extend([self.layer_colors.get(layer_type, 'black')] * nodes)
                        else:
                            # Assign a unique color to the nodes
                            node_colors.extend([self.get_unique_color()] * nodes)
            else:
                # If a layer has zero neurons, skip the layer and do not include it in the coloring process
                continue

        # Adjust the node size and line width according to the number of neurons
        max_neurons = max(num_neurons)
        if max_neurons > 40:
            node_size = 250 / max_neurons
            line_width = 1.5 / max_neurons
        else:
            node_size = 500 / max_neurons
            line_width = 3.0 / max_neurons

        ax.scatter(x_positions, y_positions, z_positions, s=node_size, c=node_colors)

        # Plot the connections between nodes
        for i in range(len(num_neurons) - 1):
            current_layer = num_neurons[i]
            next_layer = num_neurons[i + 1]

            if layer_names[i] == 'Linear' and (
                    layer_names[i + 1] != 'Linear' or i + 2 < len(layer_names) and layer_names[
                i + 2] != 'Linear') and next_layer == 0:
                next_linear_layer = self.find_next_linear_layer(layer_names, num_neurons, i + 1)
                if next_linear_layer is not None:
                    for j in range(current_layer):
                        for k in range(num_neurons[next_linear_layer]):
                            ax.plot([i, next_linear_layer], [j - offsets[i], k - offsets[next_linear_layer]], color='black', linewidth=line_width)
            else:
                for j in range(current_layer):
                    for k in range(next_layer):
                        ax.plot([i, i + 1], [j - offsets[i], k - offsets[i + 1]], color='black', linewidth=line_width)

        # Set the labels for the axes
        ax.set_xlabel('Layer')
        ax.set_ylabel('Node')
        ax.set_zlabel('')

        # Set the title of the plot
        plt.title('Neural Network Architecture')

        # Adjust the viewing angle
        if ImageViewingAngle == 'front':
            ax.view_init(elev=30, azim=1)
        elif ImageViewingAngle == 'top':
            ax.view_init(elev=56, azim=-180)
        elif ImageViewingAngle == 'left':
            ax.view_init(elev=30, azim=85)
        elif ImageViewingAngle == 'right':
            ax.view_init(elev=28, azim=-72)
        else:
            return None

        # Save the image to a file
        image_path = 'neural_network.png'
        plt.savefig(image_path)
        return image_path

    def find_next_linear_layer(self, layer_names, num_neurons, start_index):
        for i in range(start_index, len(layer_names)):
            if layer_names[i] == 'Linear' and num_neurons[i] != 0:
                return i
        return None

    def get_unique_color(self):
        for color in self.available_colors:
            if color not in self.used_colors and color not in self.layer_colors.values():
                self.used_colors.add(color)
                return color

    def run(self):
        self.app.run()


if __name__ == '__main__':
    layer_names = ['Linear', 'ReLU', 'Linear', 'Tanh', 'Linear', 'Linear']
    num_neurons = [8, 0, 8, 0, 10, 9]
    ImageViewingAngle = 'top'
    generator = NeuralNetworkGenerator()
    generator.run()
    
