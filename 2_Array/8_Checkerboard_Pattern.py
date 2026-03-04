# Write a NumPy program to create an 8x8 matrix and fill it with a checkerboard pattern.

import numpy as np

arr = np.ones((8,8),dtype=int)

print(f"Original array : \n{arr}\n")

arr[::2,::2]=0
arr[1::2,1::2]=0
print(arr)