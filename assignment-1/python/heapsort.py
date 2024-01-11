import random as r


def heapify(list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list[i] < list[left]:
        largest = left

    if right < n and list[largest] < list[right]:
        largest = right

    if largest != i:
        # Swap the elements
        list[i], list[largest] = list[largest], list[i]
        heapify(list, n, largest)


def heapsort(list):
    n = len(list)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]  # Swap
        heapify(list, i, 0)

    return list


if __name__ == "__main__":
    num = 50

    unsorted_list = [r.randint(1, num) for _ in range(num)]
    print("unsorted list: \n", unsorted_list)

    sorted_list = heapsort(unsorted_list)
    print("Sorted list: \n", sorted_list)

    other_sorted_list = sorted(unsorted_list)
    print("Other sorted list: \n", other_sorted_list)

    if other_sorted_list == sorted_list:
        print("Equal")
    else:
        print("Not equal")
