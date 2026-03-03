# Write a NumPy program to reverse an array (the first element becomes the last).

import numpy as np

arr = np.arange(1,13)

print(f"{arr}\n")

arr = arr[: : -1]

print(f"{arr}\n")
