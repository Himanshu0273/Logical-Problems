#Add an extra row to the array 

import numpy as np

arr = np.array([[10,20,30,40],[50,60,70,80]])
print(arr)

new_row = np.array([100,200,300,400])
res = np.row_stack((arr, new_row))
print(res)

ans = np.vstack((arr, new_row))
print()
print(ans)