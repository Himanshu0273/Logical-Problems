#Invert a matrix

import numpy as np

def inverse(mat):
    res = np.linalg.inv(mat)
    print(res)

x = [[12,7,3],[4,5,6],[7,8,9]]
mat = np.array(x)
inverse(mat)