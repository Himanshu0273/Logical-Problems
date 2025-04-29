#Make a 2D array with 1s on its border and 0s all rest

import numpy as np

def switch_border(mat):
    mat[1:-1, 1:-1] = 0
    print(mat)
    
def switch_body(mat):
    mat[0, :] = 1
    mat[-1,:] = 1
    mat[:, 0] = 1
    mat[:,-1] = 1
    print(mat)

mat1 = np.ones((6,6), np.int32)
mat2 = np.zeros((6,6), np.int32)
print("Ones 6x6 Matrix:\n", mat1)
print()
switch_border(mat1)
print()
print("Zeros 6x6 Matrix:\n", mat2)
print()
switch_body(mat2)