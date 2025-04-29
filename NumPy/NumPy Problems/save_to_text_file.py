#Save the numpy array in a text file

import numpy as np

ar = np.array([[1,2,3],[4,5,6]])
np.savetxt("NumPy/NumPy Problems/array_output.txt", ar, fmt="%d")
print("Array saved to file!!!")
