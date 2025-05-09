#Create a (3,4) shape array and then multiply all elements by 3

import numpy as np

arr = np.arange(12)
print(arr)
arr = arr.reshape(3,4)
print(arr)
# print(arr*3)
print()
print("Every element multiplied by 3: ")
print(arr.dot(3))