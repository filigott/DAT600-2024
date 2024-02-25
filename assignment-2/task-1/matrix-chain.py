import sys

def dynamic_matrix_chain_order(matrix_dimensions):
    num_matrices = len(matrix_dimensions) - 1
    # table m
    min_scalar_multiplications = [[0] * num_matrices for _ in range(num_matrices)]
    # table s
    optimal_splits = [[0] * num_matrices for _ in range(num_matrices)]

    # Loop over the chain lengths
    for chain_length in range(2, num_matrices + 1):
        for start_index in range(num_matrices - chain_length + 1):
            end_index = start_index + chain_length - 1
            min_scalar_multiplications[start_index][end_index] = sys.maxsize

            # Find the optimal split point within the chain
            for split_index in range(start_index, end_index):
                cost = (min_scalar_multiplications[start_index][split_index] +
                        min_scalar_multiplications[split_index + 1][end_index] +
                        matrix_dimensions[start_index] * 
                        matrix_dimensions[split_index + 1] * 
                        matrix_dimensions[end_index + 1])
                
                if cost < min_scalar_multiplications[start_index][end_index]:
                    min_scalar_multiplications[start_index][end_index] = cost
                    optimal_splits[start_index][end_index] = split_index+1

    return min_scalar_multiplications, optimal_splits

def dynamic_print_optimal_paren(optimal_splits, start, end):
    if start == end:
        print(f'A{start + 1}', end='')
    else:
        split_index = (optimal_splits[start][end])-1
        print('(', end='')
        dynamic_print_optimal_paren(optimal_splits, start, split_index)
        dynamic_print_optimal_paren(optimal_splits, split_index + 1, end)
        print(')', end='')


def greedy_matrix_chain_order(matrix_dimensions):
    num_matrices = len(matrix_dimensions) - 1
    total_multiplications = 0

    # Sort matrices by their number of columns
    sorted_matrices = sorted(range(1, num_matrices + 1), key=lambda i: matrix_dimensions[i])

    # Multiply matrices in the sorted order
    for i in range(1, num_matrices):
        total_multiplications += (matrix_dimensions[sorted_matrices[i - 1]] * 
        matrix_dimensions[sorted_matrices[i]] * 
        matrix_dimensions[sorted_matrices[-1]])

    return total_multiplications


if __name__ == "__main__":
    matrix_dimensions = [5, 15, 20, 5, 10, 25]
    dynamic_min_scalar_multiplications, optimal_splits = dynamic_matrix_chain_order(matrix_dimensions)
    print("Table m:")
    for row in dynamic_min_scalar_multiplications:
        print(" ".join("{:5}".format(value) for value in row))

    print("")

    print("Table s:")
    for row in optimal_splits:
        print(" ".join("{:5}".format(value) for value in row))

    print("")
    print("Dynamic: optimal parenthesization:")
    dynamic_print_optimal_paren(optimal_splits, 0, len(matrix_dimensions) - 2)
    print("\n")

    print("Dynamic: minimum total scalar multiplications:")
    print(dynamic_min_scalar_multiplications[0][-1])
    print("")

    greedy_total_scalar_multiplications = greedy_matrix_chain_order(matrix_dimensions)
    print("Greedy: total scalar multiplications:")
    print(greedy_total_scalar_multiplications)
