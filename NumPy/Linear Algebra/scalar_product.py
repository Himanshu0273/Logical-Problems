import numpy as np

def scalar(mat, x):
    print(mat*x)

x = [[5,1,3],[1,1,1],[1,2,1]]
y = 9
mat = np.array(x)
scalar(mat,y)