"""
array utilities
"""

from random import randint


def array_generator(min, max, arr_size=10, isRandom=True, isRandomRange=False):
    """
    Generate an array random or otherwise

    :param min: int, arrays min number
    :param max: int, arrays max number
    :param arr_size: int, default = 10, total number of items in array
    :param isRandom: bool, default = True, random number beein generated
    :param isRandomRange: bool, default = False, randome array size
    :return: array, random
    """
    if isRandom == True:
        if isRandomRange == True:
            end = randint(1, max)
        return [randint(min, max) for i in range(arr_size)]
    else:
        return [i for i in range(min, max)]


def find_largest(arr):
    """
    Find the largest item in the array

    :param arr: array
    :return: int, lagest number in array
    """

    largest = 0

    for i in range(len(arr)):
        if largest < arr[i]:
            largest = arr[i]

    return largest


# find the smallest item in the array
def find_smallest(arr):
    """
    Find the smallest item in the array

    :param arr: array
    :return: int, smallest number in array
    """

    smallest = arr[0]

    for i in range(len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]

    return smallest

