# Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a number).

import numpy as np 

arr = np.array([1,2,0,np.nan,np.inf])

print(f"Original array : {arr}")

print(f"Checking finite number or nan : {np.isfinite(arr)}")