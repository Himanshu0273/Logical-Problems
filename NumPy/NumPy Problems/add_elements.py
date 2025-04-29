#Add elements to the end of the array

import numpy as np

def add_elements(arr):
    arr = np.append(arr, 2)
    print("Adding one element: ")
    print(arr)
    lst = [9,8,7,6]
    print("Adding a list: ")
    arr = np.append(arr,lst)
    print(arr)


arr = np.array([1,2,3,4])
print("Before: ", arr)
print("After: ")
add_elements(arr)