# Write a NumPy program to compute the sum of all elements, the sum of each column and the sum of each row in a given array.

import numpy as np


arr = np.arange(1,13).reshape(3,4)

print(f"{arr}\n")

allSum = arr.sum
sumColumn1 = np.sum(arr,axis=0)
sumRow1= np.sum(arr,axis=1)

print(f"Sum of all elements is {allSum}\n sum of all column : {sumColumn1}\n sum of all rows : {sumRow1}")

