# Write a NumPy program to add, subtract, multiply, divide arguments element-wise.

import numpy as np

arr = np.arange(1,11)
arr1 = np.arange(11,21)

print(f"Array : {arr}\n")

print(f"Sum : {arr.sum()}")
print(f"Sub : {np.subtract(arr,arr1)}\n")
print(f"Multiplication : {np.multiply(arr,arr1)}\n")
print(f"Division : {np.divide(arr,arr1)}\n")

