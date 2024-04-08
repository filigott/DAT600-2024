import pulp
import networkx as nx
import matplotlib.pyplot as plt

edges = [
    ("s", "v1", 14), 
    ("s", "v2", 25), 
    ("v1", "v3", 3), 
    ("v1", "v4", 21), 
    ("v2", "v3", 13),
    ("v2", "v5", 7),
    ("v3", "v1", 6),
    ("v3", "v5", 15),
    ("v4", "v3", 5),
    ("v4", "v3", 10),
    ("v4", "t", 20),
    ("v5", "v4", 5),
    ("v5", "t", 10)
]

g = nx.DiGraph()
g.add_weighted_edges_from(edges)

prob = pulp.LpProblem("Maximum_Flow", pulp.LpMaximize)

flow = pulp.LpVariable.dicts("Flow", g.edges(), lowBound=0, cat='Continuous')

prob += pulp.lpSum(flow[("s", v)] for v in g.successors("s"))

for node in g.nodes():
    if node != "s" and node != "t":
        prob += pulp.lpSum(flow[(u, node)] for u in g.predecessors(node)) \
                == pulp.lpSum(flow[(node, v)] for v in g.successors(node))

prob += pulp.lpSum(flow[("s", v)] for v in g.successors("s")) == \
        pulp.lpSum(flow[(v, "t")] for v in g.predecessors("t"))

for u, v, c in g.edges(data='weight'):
    prob += flow[(u, v)] <= c

prob.solve()

print("Maximum Flow:", pulp.value(prob.objective))

flow_graph = g.copy()

for u, v in flow_graph.edges():
    flow_graph[u][v]['flow'] = flow[(u, v)].varValue

pos = nx.spring_layout(flow_graph)
nx.draw(flow_graph, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, arrows=True)

flow_labels = nx.get_edge_attributes(flow_graph, 'flow')
nx.draw_networkx_edge_labels(flow_graph, pos, edge_labels=flow_labels)

plt.title('Flow in the Graph')
plt.show()

