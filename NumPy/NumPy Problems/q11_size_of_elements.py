#Size of elements inside a np array

import numpy as np

arr = np.array([1,2,3], np.int64)

print("Size of array: ",arr.size)
print("Length of one element of array: ",arr.itemsize)
print("Length of array in bytes: ", arr.nbytes)