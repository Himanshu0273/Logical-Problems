#Suppress the use of scientific notations for small numbers

import numpy as np

arr = np.array([1.60000000e-10, 1.60000000e+00, 1.20000000e+03, 2.35000000e-01])

np.set_printoptions(suppress=True, precision=3)
print(arr)