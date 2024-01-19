import random as r
import math
from matplotlib import pyplot as plt

class QuickSort:
    def __init__(self):
        self.steps = 0
    
    def quicksort(self, list):
        if len(list) <= 1:
            return list

        pivot = list[len(list) // 2]

        left = []
        middle = []
        right = []

        for num in list:
            self.steps += 1
            if num < pivot:
                left.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                right.append(num)

        return self.quicksort(left) + middle + self.quicksort(right)



def quicksort(list):
    if len(list) <= 1:
        return list

    pivot = list[len(list) // 2]

    left = []
    middle = []
    right = []

    for num in list:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right.append(num)

    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    num = 6

    unsorted_list = [r.randint(1, num) for _ in range(num)]
    print("unsorted list: \n", unsorted_list)

    qs = QuickSort()
    sorted_list = qs.quicksort(unsorted_list)
    print("sorted list: \n", sorted_list)
    print("steps: ", qs.steps)
    print("expected steps: ", num * math.log(num, 2))


    # Plotting
    points = 10
    counted_steps = []
    expected_steps = []
    lengths = []

    constant = 1.1

    for i in range(points):
        length = 2**i
        unsorted_list = [r.randint(1, length) for _ in range(length)]
        qs = QuickSort()
        sorted = qs.quicksort(unsorted_list)
        print("sorted list: \n", sorted)
        counted_steps.append(qs.steps)
        lengths.append(length)
        expected = len(unsorted_list) * math.log(len(unsorted_list), 2) * constant
        expected_steps.append(expected)


    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, counted_steps, label="counted steps")
    plt.plot(lengths, expected_steps, label="expected steps")
    plt.legend()
    plt.show()
