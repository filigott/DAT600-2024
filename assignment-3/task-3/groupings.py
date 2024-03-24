import networkx as nx

def find_groups(graph):
    groups = []
    visited = set()

    for node in graph.nodes:
        if node not in visited:
            group = set()
            dfs(node, group, visited, graph)
            groups.append(group)
    
    return groups

def dfs(node, group, visited, graph):
    visited.add(node)
    group.add(node)
    
    for neighbor in graph.neighbors(node):
        if neighbor not in visited:
            dfs(neighbor, group, visited, graph)

if __name__ == "__main__":
    edges = [
        ('A', 'B'),
        ('A', 'D'),
        ('B', 'A'),
        ('B', 'C'),
        ('D', 'B'),
        ('D', 'C'),
        ('C', 'E'),
        ('C', 'F'),
        ('F', 'E'),
        ('E', 'G'),
        ('G', 'F')
    ]

    graph = nx.DiGraph()
    graph.add_edges_from(edges)

    groups = find_groups(graph)
    print("Edges:", graph.edges)
    print("Groups:", groups)
