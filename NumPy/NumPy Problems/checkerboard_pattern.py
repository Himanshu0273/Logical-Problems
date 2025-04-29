#Make a matrix that follows the checkerboard pattern (8x8 with 1 denoting white and 0 denoting black)

# mat = []
# for i in range(8):
#     row=[]
#     for j in range(8):
#         if (i+j)%2==0:
#             row.append(0)
#         else:
#             row.append(1)
#     mat.append(row)
    
    
# print(mat)

import numpy as np

def checkerboard(mat):
    mat[1::2, ::2] = 1
    mat[::2, 1::2] = 1
    print(mat)

mat = np.zeros((8,8), dtype=int)
checkerboard(mat)