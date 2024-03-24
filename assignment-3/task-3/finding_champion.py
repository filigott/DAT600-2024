import networkx as nx

def find_champions(graph):
    champions = []
    all_nodes = set(graph.nodes)
    
    for node in graph.nodes:
        reachable_nodes = set()
        dfs(node, reachable_nodes, graph)
        
        # Can reach all nodes
        if reachable_nodes == all_nodes:
            champions.append(node)
    
    return champions

def dfs(node, reachable_nodes, graph):
    reachable_nodes.add(node)
    for neighbor in graph.neighbors(node):
        if neighbor not in reachable_nodes:
            dfs(neighbor, reachable_nodes, graph)

if __name__ == "__main__":
    # Corresponding to Figure 3 in task
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

    # Find and print the champions
    champions = find_champions(graph)
    print("Edges:", graph.edges)
    print("Champions:", champions)
    print()

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

    graph = nx.DiGraph(directed_graph_adj)

    # Find and print the champions
    champions = find_champions(graph)
    print("Edges:", graph.edges)
    print("Champions:", champions)
    print()

    dag_adj = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E', 'F'],
    'D': ['E', 'F'],
    'E': ['F', 'G'],
    'F': ['G', 'H', 'J'],
    'G': [],
    'H': ['I'],
    'I': [],
    'J': ['I']
    }

    graph = nx.DiGraph(dag_adj)

    # Find and print the champions
    champions = find_champions(graph)
    print("Edges:", graph.edges)
    print("Champions:", champions)