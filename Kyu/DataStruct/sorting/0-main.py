# This is a test file for the sorting algorithms

from insertionSort import InsertionSort
from selectionSort import SelectionSort
import unittest

# Runs all the sorting algorithms
test1 = [2,1]
test2 = [5,2,3,1,4]
test3 = []

InsertionSort(test1)
InsertionSort(test2)
InsertionSort(test3)

print("insertion test1", test1)
print("insertion test2", test2)
print("insertion test3", test3)

SelectionSort(test1)

print("selection test1", test1)
print("selection test2", test2)
print("selection test3", test3)
