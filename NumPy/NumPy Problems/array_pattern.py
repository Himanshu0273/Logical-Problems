#Make a matrix that looks like:

#[[ 0. 0. 0.]
# [ 1. 0. 0.]
# [ 1. 1. 0.]
# [ 1. 1. 1.]]

import numpy as np

arr = np.tri(3,3) 
print(arr)