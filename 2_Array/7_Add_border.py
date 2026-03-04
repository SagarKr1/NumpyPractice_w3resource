# Write a NumPy program to add a border (filled with 0's) around an existing array.

import numpy as np 

arr = np.ones((3,3))

print(f"Original array : \n{arr}\n")

arr = np.pad(arr,pad_width=1,mode="constant",constant_values=0)

print(arr)