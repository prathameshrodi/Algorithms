# !/usr/bin/python3.7
"""
__author__ = "Prathamesh Rodi"
__copyright__ = "Copyright 2022"
__project__ = "Algorithms"
__version__ = "0.0.1"
__maintainer__ = "Prathamesh Rodi"
__email__ = "prathameshrodi3009@gmail.com"
"""


# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    print(f"Pivot Set as >> {pivot}")
    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            print(f"arr[l], {arr[j]}")
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(arr)
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        print(arr)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above

if __name__ == '__main__':

    arr = [10, 7, 8, 9, 1, 5]
    print(arr)
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i]),
