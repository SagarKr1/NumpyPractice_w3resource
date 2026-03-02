# Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.

import numpy as np 

arr1 = np.arange(1,11)
arr2 = np.arange(3,13)
print(f"comparing two array elemnt : {np.allclose(arr1,arr2)}\n")
print(f"comparing two array elemnt : {np.allclose(arr1,arr1)}")
