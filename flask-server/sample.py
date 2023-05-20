import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()


layers  = nn.Sequential(
    nn.Conv2d(1, 20, 5),
    nn.ReLU(),
    nn.Conv2d(20, 20, 5),
    nn.ReLU()
)

print(layers)

for layer in layers :

    if(type(layer)==nn.Conv2d):
        print(layer.weight.shape,layer.bias.shape)
    else:
        print(type(layer))


# Define the architecture of the neural network
layers = [8, 8, 8, 1]  # Number of nodes in each layer

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
c = ['blue'] * layers[0] + ['gray'] * layers[1] + ['gray'] * layers[2] + ['blue'] * layers[3]
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

# Show the plot
plt.show()