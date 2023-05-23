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
            'Softmax': 'yellow'
        }

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

        # Color the nodes based on the layer type
        node_colors = []
        for layer_type, nodes in zip(layer_names, num_neurons):
            node_colors.extend([self.layer_colors.get(layer_type, 'black')] * nodes)
        ax.scatter(x_positions, y_positions, z_positions, s=50, c=node_colors)

        # Plot the connections between nodes with the appropriate color
        for i in range(len(num_neurons) - 1):
            current_layer = num_neurons[i]
            next_layer = num_neurons[i + 1]
            layer_color = self.layer_colors.get(layer_names[i], 'black')

            for j in range(current_layer):
                for k in range(next_layer):
                    ax.plot([i, i + 1], [j - offsets[i], k - offsets[i + 1]], color=layer_color, linewidth=0.5)

                if layer_names[i] == 'Linear' and layer_names[i + 1] != 'Linear' and next_layer == 0:
                    next_linear_layer = self.find_next_linear_layer(layer_names, num_neurons, i + 1)
                    if next_linear_layer is not None:
                        ax.plot([i, next_linear_layer], [j - offsets[i], j - offsets[next_linear_layer]], color='black',
                                linewidth=0.5)

        # Set the labels for the axes
        ax.set_xlabel('Layer')
        ax.set_ylabel('Node')
        ax.set_zlabel('')

        # Set the title of the plot
        plt.title('Neural Network Architecture')

        # Adjust the viewing angle
        if ImageViewingAngle == 'front':
            ax.view_init(elev=0, azim=0)
        elif ImageViewingAngle == 'top':
            ax.view_init(elev=90, azim=0)
        elif ImageViewingAngle == 'left':
            ax.view_init(elev=0, azim=90)
        elif ImageViewingAngle == 'right':
            ax.view_init(elev=0, azim=-90)
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

    def run(self):
        self.app.run()


if __name__ == '__main__':
    layer_names = ['Linear', 'ReLU', 'Linear', 'Tanh', 'Linear']
    num_neurons = [8, 8, 8, 0, 10]
    ImageViewingAngle = 'top'
    generator = NeuralNetworkGenerator()
    generator.run()
