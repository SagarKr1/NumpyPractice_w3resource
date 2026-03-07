# Write a NumPy program to compute logarithm of the sum of exponentiations of the inputs, 
# sum of exponentiations of the inputs in base-2.

import numpy as np

l1 = np.log(1e-50)
l2 = np.log(2.5e-50)

print(f"Sum of logs : {np.logaddexp(l1,l2)}")
print(f"Sum of logs base2 : {np.logaddexp2(l1,l2)}")
