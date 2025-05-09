#Make the array immutable/read only and throw an error if operations are tried
import numpy as np

arr = np.array([1,2,3,4])
arr.setflags(write=False)
print(arr)
arr[0] = 10
print(arr)