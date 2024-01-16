import random as r
import math as m
import matplotlib.pyplot as plt


def insertion_sort(list):
    n = len(list)
    # list = list[:]  # For not modifying the underlying original unsorted list'
    steps = 0

    for i in range(1, n):
        key = list[i]
        j = i - 1
        steps += 2
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
            steps += 2
        list[j + 1] = key
        steps += 1
    return steps


if __name__ == "__main__":
    start_num = 6
    points = 10

    unsorted_list = [r.randint(1, start_num) for _ in range(start_num)]
    # unsorted_list = [5, 2, 4, 6, 1, 3]
    print("unsorted start list: ", unsorted_list)

    # sorted_list, steps = insertion_sort(unsorted_list)
    # print("sorted start list: ", sorted_list)

    # lists = [unsorted_list * 2**i for i in range(points)]
    list = unsorted_list[:]

    lengths = []

    counted_steps = []
    expected_steps = []

    constant = 0.22  # found by trial and error

    for _ in range(points):
        steps = insertion_sort(list)
        counted_steps.append(steps)

        lengths.append(len(list))

        expected = (len(list) ** 2) * constant
        # expected = steps/len(list)**2
        expected_steps.append(expected)

        list = list * 2

    print("counted steps: ", counted_steps)

    # Plotting
    plt.figure(figsize=(10, 6))
    # plt.plot([len(lst) for lst in lists], counted_steps,
    #          marker='o', label='Counted Steps')
    # plt.plot([len(lst) for lst in lists], expected_steps,
    #          linestyle='--', label='Expected Steps')
    plt.plot(lengths, counted_steps,
             marker='o', label='Counted Steps')
    plt.plot(lengths, expected_steps,
             linestyle='--', label='Expected Steps')
    plt.title('Insertion Sort Steps vs List Length')
    plt.xlabel('List Length')
    plt.ylabel('Number of Steps')
    plt.legend()
    plt.show()

    # print("expected steps:
