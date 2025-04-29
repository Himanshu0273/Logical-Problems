#Create a 3x3 matrix with range between 2 to 10

import numpy as np

mat = np.arange(2,11)
mat = mat.reshape(3,3)
print(mat)