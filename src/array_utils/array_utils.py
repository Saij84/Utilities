"""
array utilities
"""

from random import randint


# generate an array random or otherwise
def array_generator(start, end, isRandom=True, isRandomRange=False):
    if isRandom == True:
        if isRandomRange == True:
            end = randint(1, end)
        return [randint(start, end) for i in range(start, end+1)]
    else:
        return [i for i in range(start, end)]


# find the largest item in the array
def find_largest(arr):
    largest = 0

    for i in range(len(arr)):
        if largest < arr[i]:
            largest = arr[i]
    return largest


# find the smallest item in the array
def find_smallest(arr):
    smallest = arr[0]

    for i in range(len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
    return smallest

