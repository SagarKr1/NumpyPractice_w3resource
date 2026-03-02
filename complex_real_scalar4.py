#  Write a NumPy program to test element-wise for complex numbers, real numbers in a given array. 
# Also test if a given number is of a scalar type or not

import numpy as np 

arr = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])

print(f"Original array : {arr}\n")

print(f"checking complex number : {np.iscomplex(arr)}\n")
print(f"checking real number : {np.isreal(arr)}\n")
print(f"checking scaler number : {np.isscalar(3.1)} and {np.isscalar([3.1])}\n")