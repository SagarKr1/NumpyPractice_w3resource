# Write a NumPy program to find the set difference between two arrays. 
# The set difference will return sorted, distinct values in array1 that are not in array2.

import numpy as np 

arr1= np.arange(1,11)
arr2 = np.arange(1,11,2)

print(f"array 1 : \n {arr1} \n array 2 : \n {arr2}\n")

print(f"difference element : {np.setdiff1d(arr1,arr2)}")