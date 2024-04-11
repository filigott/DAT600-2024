from pulp import *

# Define the directed graph edges with capacities
edges = {
    ("s", "v1"): 14,
    ("s", "v2"): 25,
    ("v1", "v3"): 3,
    ("v1", "v4"): 21,
    ("v2", "v3"): 13,
    ("v2", "v5"): 7,
    ("v3", "v1"): 6, 
    ("v3", "v5"): 15,
    ("v4", "v3"): 10,
    ("v4", "t"): 20,
    ("v5", "v4"): 5,
    ("v5", "t"): 10
}

prob = LpProblem("Minimum_Cut", LpMinimize)

vars = LpVariable.dicts("Edge", edges.keys(), 0, 1, LpBinary)

prob += lpSum([edges[e] * vars[e] for e in edges]), "Total Cost of Cut"

prob += vars[("s", "v1")] + vars[("v1", "v3")] + vars[("v3", "v5")] + vars[("v5", "t")] >= 1
prob += vars[("s", "v1")] + vars[("v1", "v3")] + vars[("v3", "v5")] + vars[("v5", "v4")] + vars[("v4", "t")] >= 1
prob += vars[("s", "v1")] + vars[("v1", "v4")] + vars[("v4", "t")] >= 1
prob += vars[("s", "v1")] + vars[("v1", "v4")] + vars[("v4", "v3")] + vars[("v3", "v5")] + vars[("v5", "t")] >= 1
prob += vars[("s", "v2")] + vars[("v2", "v3")] + vars[("v3", "v1")] + vars[("v1", "v4")] + vars[("v4", "t")] >= 1
prob += vars[("s", "v2")] + vars[("v2", "v3")] + vars[("v3", "v5")] + vars[("v5", "v4")] + vars[("v4", "t")] >= 1
prob += vars[("s", "v2")] + vars[("v2", "v3")] + vars[("v3", "v5")] + vars[("v5", "t")] >= 1
prob += vars[("s", "v2")] + vars[("v2", "v5")] + vars[("v5", "v4")] + vars[("v4", "t")] >= 1
prob += vars[("s", "v2")] + vars[("v2", "v5")] + vars[("v5", "t")] >= 1

prob.solve()

print("Minimum cut value:", pulp.value(prob.objective))
print("Edges in the cut:")
for edge in edges:
    if pulp.value(vars[edge]) == 1:
        print(f"Edge {edge} with weight {edges[edge]}")