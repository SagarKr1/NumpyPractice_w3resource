# Write a NumPy program to append values to the end of an array.

import numpy as np

arr = np.arange(1,6)

print(f"Array : \n {arr}\n")

arr =np.append(arr,[6,7,8])

print(f"Array : \n {arr}\n")
