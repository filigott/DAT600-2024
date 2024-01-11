import random as r


def quicksort(list):
    # base case
    if len(list) <= 1:
        return list

    pivot = list[len(list) // 2]

    # Partition the list into three parts: less than, equal to, and greater than the pivot
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
    num = 50

    unsorted_list = [r.randint(1, num) for _ in range(num)]
    print("unsorted list: \n", unsorted_list)

    sorted_list = quicksort(unsorted_list)
    print("Sorted list: \n", sorted_list)

    other_sorted_list = sorted(unsorted_list)

    print("Other sorted list: \n", other_sorted_list)

    if other_sorted_list == sorted_list:
        print("Equal")
    else:
        print("Not equal")
