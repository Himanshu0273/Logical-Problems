#Save the numpy array in a text file

import numpy as np

ar1 = np.array([[1,2,3],[4,5,6]])
ar2 = np.array([[1,2,5],[4,5,7]])
file="NumPy/NumPy Problems/array_output.txt"
with open(file, 'w') as input:
    np.savetxt(input, ar1, fmt="%d")

with open(file, 'a') as input:
    np.savetxt(input, ar2, fmt="%d")