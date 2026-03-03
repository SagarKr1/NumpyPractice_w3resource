# Write a NumPy program to find the number of rows and columns in a given matrix.

import numpy as np

arr = np.arange(1,13).reshape(3,4)

print(f"{arr}")

print(f"\n size of a array : {arr.shape}")