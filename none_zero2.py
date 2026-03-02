# Write a NumPy program to test whether none of the elements of a given array are zero. 

import numpy as np

arr = np.array([1,1,2,3,4])

print(f"Elements are {arr}")

print(f"containing zeros or not ? {arr.all()}")