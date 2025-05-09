#Convert a 3x3 1s matrix to a 5x5 matrix with 0s in the border and all rest 1s

import numpy as np

def func(mat):
    mat = np.resize(mat, (5,5))
    mat[0, :] = 0
    mat[-1,:] = 0
    mat[:, 0] = 0
    mat[:,-1] = 0
    print(mat)
    # res = np.zeros((5,5), dtype=int)
    # res[1:-1, 1:-1] = mat
    # print(res)

mat = np.ones((3,3), np.int32)
print(mat)
print()
func(mat)