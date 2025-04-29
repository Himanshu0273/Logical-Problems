#Transpose of a matrix
import numpy as np
def transpose(mat):
    print(mat.T)
    
x = [[12,7,3],[4,5,6],[7,8,9]]
mat = np.array(x)
transpose(mat)