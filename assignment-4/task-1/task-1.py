import pulp as p
import matplotlib.pyplot as plt
import numpy as np

# Create a LP problem as a maximization problem
problem = p.LpProblem("Maximize_Profit", p.LpMaximize)

# Define decision variables
x = p.LpVariable('x', lowBound=0, cat='Continuous')
y = p.LpVariable('y', lowBound=0, cat='Continuous')

# Define machine and craftsman times (minutes)
machine_time_x = 15
machine_time_y = 20
craftsman_time_x = 20
craftsman_time_y = 30

# Define machine and craftsman costs
machine_cost_x = x*(100/60)*machine_time_x
machine_cost_y = y*(100/60)*machine_time_y
craftsman_cost_x = x*(20/60)*craftsman_time_x
craftsman_cost_y = y*(20/60)*craftsman_time_y

# Define total cost
total_cost = machine_cost_x + machine_cost_y + craftsman_cost_x + craftsman_cost_y

# Defining the objective function (want highest possible)
problem += (200*x + 300*y) - total_cost  # Revenue - Total cost

# Define constraints
problem += machine_time_x*x + machine_time_y*y <= 40*60  # machine production constraint
problem += craftsman_time_x*x + craftsman_time_y*y <= 35*60  # craftsman production constraint
problem += 10 <= x  # Minimum 10 units of X

# Solve the problem
problem.solve()

# Print the results
print("Optimal production quantities:")
print("Product X: {} units".format(x.varValue))
print("Product Y: {} units".format(y.varValue))
print("Total profit: {}".format(p.value(problem.objective)))


# Plot

import matplotlib.pyplot as plt
import numpy as np

# Define the range for product X and Y
x_values = np.linspace(0, 100, 120)
y_values = np.linspace(0, 100, 120)

constraint1 = (40*60 - machine_time_x*x_values) / machine_time_y  # machine time constraint
constraint2 = (35*60 - craftsman_time_x*x_values) / craftsman_time_y  # craftsman time constraint
constraint3 = np.full_like(x_values, 10)   # Minimum 10 units of X

# Define objective function
revenue = 200 * x_values + 300 * y_values
machine_cost_x = (100/60)*machine_time_x*x_values
machine_cost_y = (100/60)*machine_time_y*y_values
craftsman_cost_x = (20/60)*craftsman_time_x*x_values
craftsman_cost_y = (20/60)*craftsman_time_y*y_values
total_cost = machine_cost_x + machine_cost_y + craftsman_cost_x + craftsman_cost_y
profit = revenue - total_cost

# Create meshgrid for X and Y values
X, Y = np.meshgrid(x_values, y_values)

# Calculate profit on the meshgrid
profit_grid = 200 * X + 300 * Y - total_cost

# Plot constraints and feasible region
plt.figure(figsize=(16, 12))
plt.plot(x_values, constraint1, label='Machine Time Constraint')
plt.plot(x_values, constraint2, label='Craftsman Time Constraint')
plt.axvline(x=10, color='r', linestyle='--', label='Minimum 10 units of X')  # Minimum 10 units of X constraint
plt.fill_between(x_values, np.maximum(constraint1, constraint3), where=(constraint1 >= constraint3), color='gray', alpha=0.5)
plt.fill_between(x_values, np.maximum(constraint2, constraint3), where=(constraint2 >= constraint3), color='gray', alpha=0.5)

# Plot the contour plot of the profit function
plt.contourf(X, Y, profit_grid, levels=20, cmap='viridis', alpha=0.5)

# Add labels and legend
plt.xlabel('Product X')
plt.ylabel('Product Y')
plt.title('Optimization Problem')
plt.legend()

# Show plot
plt.colorbar(label='Profit')
plt.grid(True)
plt.show()
