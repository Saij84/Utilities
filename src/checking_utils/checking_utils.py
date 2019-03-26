"""
checking utilities
"""


def growing_num(arr):
    """
    Attempt to make sure that the array is sorted

    :param arr: take an array
    :return: string
    """

    largets = arr[-1]

    for i in range(len(arr)):
        if arr[i] > largets:
            return "The array provided was not sorted in an incremental way, error at index: {}".format(i)
    return "The array provided is a sorted array"
