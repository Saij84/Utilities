"""
sorting utilities
"""
from utils.src.array_utils import array_utils as aUtils

# merge sorting, first part: divide the given array to its smallest parts
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


# merging function
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


def partition(arr, l_idx, r_idx):
    x = arr[l_idx]
    j = l_idx

    for i in range(l_idx+1, r_idx):
        if arr[i] <= x:
            j += 1

            arr[j], arr[i] = arr[i], arr[j]
    arr[l_idx], arr[j] = arr[j], arr[l_idx]
    return j


def quick_sort(arr):
    l_idx, r_idx = 0, len(arr)

    if l_idx >= r_idx:
        return

    m = partition(arr, l_idx, r_idx)

    quick_sort(arr[:m-1])
    quick_sort(arr[m+1:])

    return arr

x=9

for i in range(1):
    data_in = aUtils.array_generator(1, 100, arr_size=x, isRandomRange=False)
    print(data_in)
    print(quick_sort(data_in))