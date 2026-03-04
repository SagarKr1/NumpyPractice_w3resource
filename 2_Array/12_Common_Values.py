# Write a NumPy program to find common values between two arrays.

import numpy as np 

arr1= np.arange(1,11)
arr2 = np.arange(1,11,2)

print(f"array 1 : \n {arr1} \n array 2 : \n {arr2}\n")

print(f"extracting command element : {arr1[np.isin(arr1,arr2)]}")