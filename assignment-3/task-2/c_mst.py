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
    for edge in edges:
        u, v, _ = edge
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

    mst_variants =[]

    original_weights = [edge[2] for edge in edges]

    mst_variants = []

    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            # Swap the weights of two edges.
            swapped_edges = edges.copy()
            swapped_edges[i] = (edges[i][0], edges[i][1], edges[j][2])
            swapped_edges[j] = (edges[j][0], edges[j][1], edges[i][2])
            what_swapped = (edges[i], edges[j])
            # Calculate MST for the graph with swapped weights.
            mst_result = mst(swapped_edges)
            total_cost = sum(edge[2] for edge in mst_result)

            # Store the MST and its total cost.
            mst_variants.append((mst_result, total_cost, what_swapped))

    min_cost = min(mst_variants, key=lambda x: x[1])

    print(f"Minimum cost: {min_cost[1]}")
    print("MST:")
    print(min_cost[0])
    print("Swapped edges:")
    print(min_cost[2])
    plot(min_cost[0])