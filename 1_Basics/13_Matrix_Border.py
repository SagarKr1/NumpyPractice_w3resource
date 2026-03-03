# Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.

import numpy as np 

arr = np.ones((10,10))

print(f"{arr}\n")

arr[1:-1,1:-1]=0

print(f"{arr}\n")

# arr[2:-2,2:-2]=1

# print(f"{arr}\n")