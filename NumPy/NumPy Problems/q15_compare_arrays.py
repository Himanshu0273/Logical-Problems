#Compare 2 arrays 

import numpy as np

ar1 = np.array([1,2,3,4])
ar2 = np.array([3,1,2,4])

print("Array 1:", ar1)
print("Array 2:", ar2)
print()
print("ar1 > ar2: ", end=" ")
res = ar1>ar2
print(res)

print()
print("ar1 < ar2: ", end=" ")
res = ar1<ar2
print(res)

res = ar1>=ar2
print()
print("ar1 >= ar2: ", end=" ")
print(res)

res = ar1<=ar2
print()
print("ar1 <= ar2: ", end=" ")
print(res)
