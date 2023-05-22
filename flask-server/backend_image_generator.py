from flask import Flask, send_file
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend


class NeuralNetworkGenerator:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/generate_neural_network', 'generate_neural_network', self.generate_neural_network_route)

    def generate_neural_network_route(self):
        # Generate the neural network image
        image_path = self.generate_neural_network(layers, perspective)

        # Send the image file to the frontend
        return send_file(image_path, mimetype='image/png')

    def generate_neural_network(self, layers, perspective):
        # Calculate the offset for centering the circles within each layer
        offsets = [nodes / 2 - 0.5 for nodes in layers]

        # Create a figure and a 3D subplot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the nodes
        x_positions = []
        y_positions = []
        z_positions = []

        for layer, nodes in enumerate(layers):
            x_positions.extend([layer] * nodes)
            y_positions.extend(range(nodes))
            z_positions.extend([0] * nodes)  # Set z-coordinate to 0 for all nodes

            # Apply the offset to center the circles within each layer
            y_positions[-nodes:] = np.array(y_positions[-nodes:]) - offsets[layer]

        # Color the first layer differently
        c = ['blue'] * layers[0] + ['gray'] * sum(layers[1:-1]) + ['blue'] * layers[-1]
        ax.scatter(x_positions, y_positions, z_positions, s=50, c=c)

        # Plot the connections between nodes
        for i in range(len(layers) - 1):
            current_layer = layers[i]
            next_layer = layers[i + 1]

            for j in range(current_layer):
                for k in range(next_layer):
                    ax.plot([i, i + 1], [j - offsets[i], k - offsets[i + 1]], [0, 0], color='black', linewidth=0.5)

        # Set the labels for the axes
        ax.set_xlabel('Layer')
        ax.set_ylabel('Node')
        ax.set_zlabel('')

        # Set the title of the plot
        plt.title('Neural Network Architecture')

        # Adjust the viewing perspective
        if perspective == 'front':
            ax.view_init(elev=0, azim=0)
        elif perspective == 'top':
            ax.view_init(elev=90, azim=0)
        elif perspective == 'left':
            ax.view_init(elev=0, azim=90)
        elif perspective == 'right':
            ax.view_init(elev=0, azim=-90)
        else:
            print('Invalid perspective!')

        # Save the image to a file
        image_path = 'neural_network.png'
        plt.savefig(image_path)

        return image_path

    def run(self):
        self.app.run()


layers = [8, 8, 8, 1]  # Example of number of nodes in each layer
perspective = 'left'  # Example of perspective for the visualization

if __name__ == '__main__':
    generator = NeuralNetworkGenerator()
    generator.run()
