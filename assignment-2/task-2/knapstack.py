import random

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.unit_value = value / weight

def generate_items(n, unit):
    items = []
    for _ in range(n):
        weight = random.randint(1, 20)
        if unit == 'kg':
            value = random.randint(1, 50)
        elif unit == 'price':
            value = random.randint(10, 100)
        else:
            raise ValueError("Invalid unit. Use 'kg' or 'price'")
        items.append(Item(weight, value))
    return items

def generate_0_1_knapsack_problem(items, capacity):
    n = len(items)
    # Create a table to store values for dynamic programming
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if items[i - 1].weight <= j:
                dp[i][j] = max(dp[i - 1][j], items[i - 1].value + dp[i - 1][j - items[i - 1].weight])
            else:
                dp[i][j] = dp[i - 1][j]

    # Reconstruct the items that are chosen
    knapsack = [0] * n
    total_weight = capacity
    total_value = dp[n][capacity]
    for i in range(n, 0, -1):
        if dp[i][total_weight] != dp[i - 1][total_weight]:
            knapsack[i - 1] = 1
            total_weight -= items[i - 1].weight

    return knapsack, capacity - total_weight, total_value

def generate_fractional_knapsack_problem(items, capacity):
    n = len(items)
    total_weight = 0
    total_value = 0

    items_sorted = sorted(items, key=lambda x: x.unit_value, reverse=True)

    fractions = [0] * n
    for item in items_sorted:
        if total_weight + item.weight <= capacity:
            fractions[items.index(item)] = 1
            total_weight += item.weight
            total_value += item.value
        else:
            remaining_capacity = capacity - total_weight
            fraction = remaining_capacity / item.weight
            fractions[items.index(item)] = fraction
            total_weight += remaining_capacity
            total_value += fraction * item.value
            break
    
    return fractions, total_weight, total_value

def print_problem(items, knapsack, total_weight, total_value):
    print("Items:")
    for item in items:
        print(f"Weight: {item.weight}, Value: {item.value}")

    print("\nKnapsack:")
    for i, item in enumerate(items):
        if knapsack[i] == 1:
            print(f"Weight: {item.weight}, Value: {item.value}")
        elif knapsack[i] > 0 and knapsack[i] < 1:
            print(f"Original: Weight: {item.weight}, Value: {item.value} --> Fraction: Weight: {item.weight * knapsack[i]}, Value: {item.value * knapsack[i]}")

    print(f"\nTotal Weight: {total_weight}, Total Value: {total_value}")

if __name__ == "__main__":
    number_of_problems = int(input("Enter the number of problems: "))
    for i in range(number_of_problems):
        print(f"------------------------------------ PROBLEM {i+1} ------------------------------------")
        unit = input("Enter the unit type (kg or price): ")
        capacity = int(input("Enter the maximum capacity of the knapsack: "))
        n = int(input("Enter the number of items: "))

        items = generate_items(n, unit)
        print(f"------------------------------------ PROBLEM {i+1} SOLUTION ------------------------------------")
        print("\n0-1 Knapsack Problem:")
        knapsack, total_weight, total_value = generate_0_1_knapsack_problem(items, capacity)
        print_problem(items, knapsack, total_weight, total_value)

        print("\nFractional Knapsack Problem:")
        fractions, total_weight, total_value = generate_fractional_knapsack_problem(items, capacity)
        print_problem(items, fractions, total_weight, total_value)
