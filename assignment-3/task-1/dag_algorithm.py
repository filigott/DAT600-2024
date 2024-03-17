import networkx as nx
import matplotlib.pyplot as plt

def remove_cycles(graph):
    graph = graph.copy()
    removed_edges = []

    def dfs(node, visited, current_path):
        visited.add(node)
        current_path.add(node)

        for neighbor in graph:
            if neighbor[0] == node:
                child = neighbor[1]
                if child in current_path:
                    removed_edges.append((node, child))
                    graph.remove((node, child))
                elif child not in visited:
                    dfs(child, visited, current_path)

        current_path.remove(node)

    visited = set()
    for node in graph:
        if node[0] not in visited:
            dfs(node[0], visited, set())

    return graph, removed_edges


def transform_to_tuple_format(graph):
    tuple_graph = []
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            tuple_graph.append((node, neighbor))
    return tuple_graph


def graph_has_cycles(dag):
    try:
        nx.find_cycle(dag, orientation='original')
        return True
    except nx.NetworkXNoCycle:
        return False
    

directed_graph_adj = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E', 'F'],
    'D': ['E', 'F'],
    'E': ['F', 'G'],
    'F': ['B', 'G', 'H', 'J'],
    'G': [],
    'H': ['I'],
    'I': [],
    'J': ['I']
}

# Additional edges
directed_graph_adj['I'].append('C')
directed_graph_adj['J'].append('A')

graph = transform_to_tuple_format(directed_graph_adj)

dag, removed_edges = remove_cycles(graph)
print("Original Graph:", graph)
print("Removed Edges:", removed_edges)
print("Transformed DAG:", dag)

G = nx.DiGraph(graph)
DAG = nx.DiGraph(dag)

print("Proving the results using networkx...")

has_cycles = graph_has_cycles(G)
if has_cycles:
    print("The original graph contains cycles.")
else:
    print("The original graph is acyclic.")

has_cycles = graph_has_cycles(DAG)
if has_cycles:
    print("The transformed DAG contains cycles.")
else:
    print("The transformed DAG is acyclic.")


spacing = 5

# Define the layout once for both plots
pos = nx.spring_layout(G, k=spacing)

plt.figure(figsize=(24, 12))

# Plotting original graph in subplot 1
plt.subplot(121)
nx.draw_networkx(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12)
plt.title('Original Graph')

# Plotting transformed DAG in subplot 2
plt.subplot(122)
nx.draw_networkx(DAG, pos, with_labels=True, node_size=1000, node_color='lightgreen', font_size=12)
plt.title('Transformed DAG')

plt.tight_layout()  # Adjust layout to prevent overlapping

# Save the graph as an image
# plt.savefig("assignment-3/task-1/dag_graph.png")

plt.show()


