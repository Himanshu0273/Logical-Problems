#COnvert the given np array to python list with all decimals being rounded off to 3 decimal places

import numpy as np

arr = np.array([ 0.26153123, 0.52760141, 0.5718299, 0.5927067, 0.7831874, 0.69746349, 0.35399976, 0.99469633, 0.0694458, 0.54711478])
print(arr)
print()
np.set_printoptions(precision=3)
print("Not actually changing the values: ",arr)
print()
arr = np.round(arr, 3)
lst = arr.tolist()
print("Actually changing the values: ",lst)