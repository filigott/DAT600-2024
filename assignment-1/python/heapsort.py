import random as r
import math as m
import matplotlib.pyplot as plt


def heapify(list, n, i, steps):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        steps += 1

        if list[i] < list[left]:
            largest = left

    if right < n:
        steps += 1

        if list[largest] < list[right]:
            largest = right

    if largest != i:
        # Swap the elements
        list[i], list[largest] = list[largest], list[i]
        steps = heapify(list, n, largest, steps)

    return steps


def heapsort(list):
    n = len(list)
    steps = 0

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        steps += 1
        steps = heapify(list, n, i, steps)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        steps += 1
        list[i], list[0] = list[0], list[i]  # Swap
        steps = heapify(list, i, 0, steps)

    return list, steps


if __name__ == "__main__":
    start_num = 10
    points = 10

    unsorted_list = [r.randint(1, start_num) for _ in range(start_num)]
    print("unsorted start list:", unsorted_list)

    sorted_list, steps = heapsort(unsorted_list)
    print("Sorted start list: ", sorted_list)

    lists = [unsorted_list * 2**i for i in range(points)]

    counted_steps = []
    expected_steps = []

    constant = 1.7  # found by trial and error

    for list in lists:
        _, steps = heapsort(list)
        counted_steps.append(steps)

        expected = (len(list) * m.log2(len(list))) * constant
        expected_steps.append(expected)

    print("counted steps: ", counted_steps)

    # Plotting
   # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot([len(lst) for lst in lists], counted_steps,
             marker='o', label='Heapsort Steps')
    plt.plot([len(lst) for lst in lists], expected_steps,
             linestyle='--', color='r', label='Expected Steps')
    plt.title('Heapsort Steps vs List Length')
    plt.xlabel('List Length')
    plt.ylabel('Number of Steps')
    plt.legend()
    plt.show()
