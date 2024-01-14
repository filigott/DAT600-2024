import random as r


def insertion_sort(list):
    n = len(list)
    list = list[:]  # For not modifying the underlying original unsorted list'
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
    return list, steps


if __name__ == "__main__":
    num = 10

    unsorted_list = [r.randint(1, num) for _ in range(num)]
    print("unsorted list: ", unsorted_list)

    sorted_list, steps = insertion_sort(unsorted_list)
    print("sorted list: ", sorted_list)


    print("steps: ", steps)

    print("expected steps: ", num * (num - 1) / 2 + 3 * (num - 1) + 1)
