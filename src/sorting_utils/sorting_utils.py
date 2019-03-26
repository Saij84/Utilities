"""
sorting utilities
"""
from random import random


<<<<<<< HEAD
=======
# merge sorting, first part: divide the given array to its smallest parts
# merge sorting is an recursive sort meaning it will take more memory depending on the size of the array
# then use the a merge function to put the array back together in ascending order
>>>>>>> 221267a7444136413eba6fdd47ee952f8e84d9da
def merge_sort(arr):
    """
    Merge sorting, first part: divide the given array to its smallest parts
    then use the a merge function to put the array back together in ascending order

    :param arr: array
    :return: sorted array
    """

    array_len = len(arr)
    if array_len <= 1:
        return arr

    left, right, result = [], [], []

    for idx in range(array_len):
        if idx < array_len//2:  # if value i is smaller than the dividing point
            left.append(arr[idx])
        else:
            right.append(arr[idx])

    left = merge_sort(left)
    right = merge_sort(right)
    result = merge(left, right)

    return result


<<<<<<< HEAD
=======
# merge sort, merging function
>>>>>>> 221267a7444136413eba6fdd47ee952f8e84d9da
def merge(left, right):
    """
    Merging function for merge sort

    :param left: array
    :param right: array
    :return: sorted array
    """
    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:  # run when there are items in both lef and right arrays
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:  # catch left leftovers
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0: # catch right leftovers
            result.append(right[0])
            right = right[1:]

    return result


<<<<<<< HEAD
def partition(arr, l_idx, r_idx):
    """
    Partition function for random quick sort to sort the incoming sub arrays

    :param arr: array
    :param l_idx: start of array
    :param r_idx: end of array
    :return: sorted array
    """

    pivot, l_idx, r_idx = arr[l_idx], l_idx, r_idx
    idx = l_idx

    while idx <= r_idx:
        if arr[idx] < pivot:
            arr[l_idx], arr[idx] = arr[idx], arr[l_idx]
            l_idx += 1

        elif arr[idx] > pivot:
            arr[r_idx], arr[idx] = arr[idx], arr[r_idx]
            r_idx -= 1
            idx -= 1
        idx += 1

    return l_idx, r_idx


def randomized_quick_sort(arr, l_idx, r_idx):
    """
    Main of randomized quicksort
=======
# quick sort, sort items according to an pivot item that satisfies condition: l <= pivot < r
# and recursively sort "left"/"right" side of the pivot
# quick sort is and in-place sorting algorithm(memory efficient)
def quick_sort(arr, l_idx, r_idx):
    if l_idx >= r_idx:
        return arr

    m = partition(arr, l_idx, r_idx)

    quick_sort(arr, l_idx, m)  # sort "left" side of pivot
    quick_sort(arr, m+1, r_idx)  # sort "right" side of the pivot
>>>>>>> 221267a7444136413eba6fdd47ee952f8e84d9da

    :param arr: array
    :param l_idx: int, start of array
    :param r_idx: int, end of array
    :return: sorted array
    """

    if l_idx >= r_idx:
        return

    r_num = random.randint(l_idx, r_idx)
    arr[l_idx], arr[r_num] = arr[r_num], arr[l_idx]

    m1, m2 = partition(arr, l_idx, r_idx)

<<<<<<< HEAD
    randomized_quick_sort(arr, l_idx, m1)
    randomized_quick_sort(arr, m2 + 1, r_idx)

    return arr
=======
# quick sort sub-process sorting the array(in place)
def partition(arr, l_idx, r_idx):
    pivot = arr[l_idx]  # set pivot item, always set to l_idx
    p_idx = l_idx  # pivot item idx count

    for idx in range(l_idx+1, r_idx):  # iterate through the indexes
        if arr[idx] <= pivot:
            p_idx += 1
            arr[p_idx], arr[idx] = arr[idx], arr[p_idx]  # in place switching
    arr[l_idx], arr[p_idx] = arr[p_idx], arr[l_idx]  # move pivot item to correct index

    return p_idx
>>>>>>> 221267a7444136413eba6fdd47ee952f8e84d9da
