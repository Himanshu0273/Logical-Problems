#3D Array with diagonals 1 and all the other elements being 0

import numpy as np

# arr = np.identity(3)
# print(arr)

a3 = np.array([np.eye(3) for _ in range(2)])
print(a3)