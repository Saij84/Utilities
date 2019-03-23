"""
sorting utilities
"""
from utils.src.array_utils import array_utils as aUtils

# merge sorting, first part: divide the given array to its smallest parts
# merge sorting is an recursive sort meaning it will take more memory depending on the size of the array
# then use the a merge function to put the array back together in ascending order
def merge_sort(arr):
    array_len = len(arr)
    if array_len <= 1:
        return arr

    left, right, result = [], [], []

    for i in range(array_len):
        if i < array_len//2:  # if value i is smaller than the dividing point
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = merge_sort(left)
    right = merge_sort(right)
    result = merge(left, right)

    return result


# merge sort, merging function
def merge(left, right):
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


# quick sort, sort items according to an pivot item that satisfies condition: l <= pivot < r
# and recursively sort "left"/"right" side of the pivot
# quick sort is and in-place sorting algorithm(memory efficient)
def quick_sort(arr, l_idx, r_idx):
    if l_idx >= r_idx:
        return arr

    m = partition(arr, l_idx, r_idx)

    quick_sort(arr, l_idx, m)  # sort "left" side of pivot
    quick_sort(arr, m+1, r_idx)  # sort "right" side of the pivot

    return arr


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
