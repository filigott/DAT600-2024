import random as r
import time as t
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

    num_points = 10
    start_num = 6
    execution_time_list = []
    lengths_list = []

    for i in range(num_points):
        n = start_num * (2**i)
        l = [r.randint(1, n) for _ in range(n)]
        time_start = t.time()
        _ = insertion_sort(l)
        time_end = t.time()
        print("Done with list of length: ", len(l))
        execution_time_list.append(time_end - time_start)
        lengths_list.append(len(l))

    plt.figure(figsize=(10, 6))
    plt.plot(lengths_list, execution_time_list)
    # plt.xticks(lengths_list)
    plt.xlabel("Length of list")
    plt.ylabel("Execution time")
    plt.title("Execution time of insertion sort")
    plt.show()
