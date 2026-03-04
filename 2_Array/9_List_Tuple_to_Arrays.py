# Write a NumPy program to convert a list and tuple into arrays.

import numpy as np

lst = [1,2,3,4,5]
tpl = (1,2,3,4,5)

print(f"List : {type(lst)} and Tuple : {type(tpl)}")

arr = np.array(lst)

print(f"list to array : {arr}\n")

arr = np.array(tpl)

print(f"tuple to array : {arr}\n")
