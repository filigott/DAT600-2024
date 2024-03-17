import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix
adjacency_matrix = np.array([
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
])

# Create a networkx graph from the adjacency matrix
G = nx.from_numpy_matrix(adjacency_matrix)

# Define mapping for node labels
node_labels_mapping = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6'}

# Set the figure size
plt.figure(figsize=(10, 8))

# Draw the graph
pos = nx.spring_layout(G) 
nx.draw_networkx(G, pos, labels=node_labels_mapping, with_labels=True, node_color='skyblue', node_size=1500, edge_color='k', linewidths=1, font_size=15)

plt.title("Graph Representation of Adjacency Matrix")

# Save the graph as an image
# plt.savefig("assignment-3/task-1/adjacency_graph.png")

# Display the graph
plt.show()
