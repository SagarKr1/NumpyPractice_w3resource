# Write a NumPy program to find the union of two arrays.
# Union will return a unique, sorted array of values in each of the two input arrays.

import numpy as np


arr1 = np.arange(1, 11)
arr2 = np.arange(1, 11, 2)

print(f"array 1 : \n {arr1} \n array 2 : \n {arr2}\n")


print(f"Union of array : {np.union1d(arr1,arr2)}")
