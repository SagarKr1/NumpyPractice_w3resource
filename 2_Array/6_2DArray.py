# Write a NumPy program to create a 2D array with 1 on the border and 0 inside.

import numpy as np 

arr = np.ones((10,10))

print(f" Original array : \n {arr}\n")

arr[1:-1,1:-1]=0

print(f"{arr}")