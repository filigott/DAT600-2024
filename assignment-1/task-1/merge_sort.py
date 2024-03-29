import random as r
from matplotlib import pyplot as plt
import math


class MergeSort:
    def __init__(self):
        self.steps = 0
    
    def merge_sort(self, list):
        # base case for the recursion
        if len(list) <= 1:
            return list

        # split the list into two parts
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]

        # sort both parts recursively
        self.merge_sort(left_half)
        self.merge_sort(right_half)

        # merge the two sorted parts together
        self.merge(list, left_half, right_half)

        return list
    
    def merge(self, list: [], left_half: [], right_half: []):
        # pointers to indices in list
        p_left = 0
        p_right = 0
        p_list = 0

        while p_left < len(left_half) and p_right < len(right_half):
            self.steps += 1
            if left_half[p_left] < right_half[p_right]:
                list[p_list] = left_half[p_left]
                p_left += 1
            else:
                list[p_list] = right_half[p_right]
                p_right += 1
            p_list += 1

        # copy the remaining elements of left_half
        while p_left < len(left_half):
            self.steps += 1
            list[p_list] = left_half[p_left]
            p_left += 1
            p_list += 1

        # copy the remaining elements of right_half
        while p_right < len(right_half):
            self.steps += 1
            list[p_list] = right_half[p_right]
            p_right += 1
            p_list += 1

def merge_sort(list):
    # base case for the recursion
    if len(list) <= 1:
        return list

    # split the list into two parts
    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]

    # sort both parts recursively
    merge_sort(left_half)
    merge_sort(right_half)

    # merge the two sorted parts together
    merge(list, left_half, right_half)

    return list


def merge(list: [], left_half: [], right_half: []):
    # pointers to indices in list
    p_left = 0
    p_right = 0
    p_list = 0

    while p_left < len(left_half) and p_right < len(right_half):
        if left_half[p_left] < right_half[p_right]:
            list[p_list] = left_half[p_left]
            p_left += 1
        else:
            list[p_list] = right_half[p_right]
            p_right += 1
        p_list += 1

    # copy the remaining elements of left_half
    while p_left < len(left_half):
        list[p_list] = left_half[p_left]
        p_left += 1
        p_list += 1

    # copy the remaining elements of right_half
    while p_right < len(right_half):
        list[p_list] = right_half[p_right]
        p_right += 1
        p_list += 1


if __name__ == "__main__":
    num = 6

    unsorted_list = [r.randint(1, num) for _ in range(num)]
    print("unsorted list: \n", unsorted_list)

    ms = MergeSort()
    sorted_list = ms.merge_sort(unsorted_list)
    print("sorted list: \n", sorted_list)
    print("steps: ", ms.steps)
    print("expected steps: ", num * math.log(num, 2))


    # Plotting
    points = 10
    counted_steps = []
    expected_steps = []
    lengths = []

    constant = 1.05

    for i in range(points):
        length = num * 2**i
        unsorted_list = [r.randint(1, length) for _ in range(length)]
        print("unsorted list: \n", unsorted_list) 
        ms = MergeSort()
        sorted = ms.merge_sort(unsorted_list)
        print("sorted list: \n", sorted)
        counted_steps.append(ms.steps)
        lengths.append(length)
        expected = len(unsorted_list) * math.log(len(unsorted_list), 2) * constant
        expected_steps.append(expected)


    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, counted_steps, label="counted steps")
    plt.plot(lengths, expected_steps, label="expected steps")
    plt.xlabel("length of list")
    plt.ylabel("steps")
    plt.title("Merge Sort")
    plt.legend()
    plt.show()