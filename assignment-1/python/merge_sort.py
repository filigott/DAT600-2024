import random as r


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
    num = 50

    unsorted_list = [r.randint(1, num) for _ in range(num)]
    print("Unsorted list:", unsorted_list)

    sorted_list = merge_sort(unsorted_list)
    print("Sorted list:", sorted_list)

    other_sorted_list = sorted(unsorted_list)

    print("Other sorted list: ", other_sorted_list)

    if other_sorted_list == sorted_list:
        print("Equal")
    else:
        print("Not equal")
