#Concatenate 2 matrices

import numpy as np

arr1 = np.array([[0, 1, 3], [5, 7, 9]])
arr2 = np.array([[0, 2, 4], [6, 8, 10]])
arr3 = np.concatenate((arr1,arr2),axis=1)
print(arr3)
print()
arr3 = np.concatenate((arr1,arr2),axis=0)
print(arr3)