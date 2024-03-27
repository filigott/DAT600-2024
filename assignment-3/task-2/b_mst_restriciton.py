class UnionFind:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1

def mst(edges):
    edges.sort(key=lambda x: x[2])
    vertices = set([u for u, v, _ in edges] + [v for u, v, _ in edges])
    uf = UnionFind(vertices)
    mst = []
    edge_count_for_D = 0
    max_edges_for_D = 3
    for edge in edges:
        u, v, _ = edge
        if u == 'D' or v == 'D':
            if edge_count_for_D >= max_edges_for_D:
                continue
            else:
                edge_count_for_D += 1
                
        if uf.find(u) != uf.find(v):
            mst.append(edge)
            uf.union(u, v)
    return mst

def plot(edges):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size=700)

    nx.draw_networkx_edges(G, pos, width=2)

    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=20)

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    edges = [
    ('A', 'B', 5),
    ('A', 'D', 1),
    ('B', 'D', 4),
    ('B', 'H', 8),
    ('D', 'C', 2),
    ('D', 'E', 2),
    ('D', 'F', 4),
    ('C', 'G', 6),
    ('E', 'H', 8),
    ('F', 'G', 9),
    ('F', 'H', 7)
    ]
    mst_edges = mst(edges)

    total_cost = sum([weight for _, _, weight in mst_edges])
    b = 30
    within_budget = total_cost <= b

    print(f"Total cost: {total_cost}")
    print(f"Within budget: {within_budget}")

    plot(mst_edges)