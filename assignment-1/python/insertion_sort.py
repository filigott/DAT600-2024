import random as r


def insertion_sort(list):
    n = len(list)
    list = list[:]  # For not modifying the underlying original unsorted list

    for i in range(1, n):
        key = list[i]
        j = i - 1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key
    return list


if __name__ == "__main__":
    num = 50

    unsorted_list = [r.randint(1, num) for _ in range(num)]
    print("unsorted list: ", unsorted_list)

    sorted_list = insertion_sort(unsorted_list)
    print("sorted list: ", sorted_list)
