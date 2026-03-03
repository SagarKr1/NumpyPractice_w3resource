# Write a NumPy program to create a 3X4 array and iterate over it.

import numpy as np 

arr = np.arange(1,13).reshape(3,4)

print(f"array elemnts are : \n {arr}")

# for i in arr:
#     for j in i:
#         print(j)

for i in np.nditer(arr):
    print(i,end=" ")