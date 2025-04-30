#Remove the first, fourth and fifth element from a numpy array

import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90])

# arr = np.delete(arr, 0)
# arr = np.delete(arr, 3)
# arr = np.delete(arr, 4)
index_to_remove = [0,3,4]
# arr = np.delete(arr, index_to_remove)
print(arr)

arr = np.delete(arr, np.where(arr>50))
print(arr)
print()

#Remove a row and column from a 2D array
mat = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(mat)
print()
r = np.delete(mat, (3,4))
print(r)
row = np.delete(mat,0,axis=0)
col = np.delete(mat,1,axis=1)
print()
print(row)
print()
print(col)
