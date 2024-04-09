from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Define the directed graph edges with capacities
edges = [
    ("s", "v1", 14), 
    ("s", "v2", 25), 
    ("v1", "v3", 3), 
    ("v1", "v4", 21), 
    ("v2", "v3", 13),
    ("v2", "v5", 7),
    ("v3", "v1", 6),
    ("v3", "v5", 15),
    ("v4", "v3", 10),
    ("v4", "t", 20),
    ("v5", "v4", 5),
    ("v5", "t", 10)
]

# Initialize the problem
problem = LpProblem("Maximum_Flow", LpMaximize)

# For each edge, create an LP variable that represents the flow through that edge
flows = { (u, v): LpVariable(f"f_{u}_{v}", lowBound=0, upBound=c, cat='Continuous')
          for u, v, c in edges }

# The objective is to maximize the total flow into the sink node t. This line adds the objective function to the problem, which sums all flows into t.
problem += lpSum([flows[edge] for edge in flows if edge[1] == 't']), "Maximize_Flow"

nodes = set([u for u, v, c in edges] + [v for u, v, c in edges])
nodes -= set(['s', 't']) # Remove source and sink

# For every node except the source s and sink t, we make sure inflow == outflow. This maintains the conservation of flow at each node.
for node in nodes:
    problem += (
        lpSum([flows[(u, v)] for u, v in flows if v == node]) ==
        lpSum([flows[(u, v)] for u, v in flows if u == node]),
        f"Flow_Conservation_{node}"
    )

# Solve the problem
problem.solve()

# Display the optimal flow values
optimal_flows = {edge: flow.value() for edge, flow in flows.items()}
optimal_total_flow = sum(flow.value() for edge, flow in flows.items() if edge[1] == 't')

print("Optimal Total Flow:", optimal_total_flow)
