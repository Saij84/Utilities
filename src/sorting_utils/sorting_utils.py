"""
sorting utilities
"""

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
