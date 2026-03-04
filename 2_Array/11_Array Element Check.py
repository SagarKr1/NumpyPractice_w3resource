# Write a NumPy program to test whether each element of a 1-D array is also present in a second array.

import numpy as np

arr1= np.arange(1,11)
arr2 = np.arange(1,11,2)

print(f"array 1 : \n {arr1} \n array 2 : \n {arr2}\n")

print(f"Check element : {np.isin(arr1,arr2)} \n")