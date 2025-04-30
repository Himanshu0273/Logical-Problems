#Add an extra column to the array

import numpy as np

arr = np.array([[10,20,30,40],[50,60,70,80]])
print(arr)
print()

new_col = np.array([100 ,200])
res=np.column_stack((arr,new_col))
print(res)
print()

ans = np.hstack((arr, [[100],[200]]))
print(ans)