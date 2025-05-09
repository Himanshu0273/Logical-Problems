#Convert a numpy 2D array to a list

import numpy as np

arr = np.arange(6)
arr = arr.reshape(3,-1)
print(arr)

lst = arr.tolist()
print(lst)
print(type(lst))