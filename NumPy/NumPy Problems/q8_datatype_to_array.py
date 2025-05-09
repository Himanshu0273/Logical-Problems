#Convert a list to array and a tuple to array
import numpy as np

def tuple_to_arr(tup):
    arr = np.array(tup)
    print(arr)
    print("Type of tuple now: ", type(arr))

def list_to_arr(lst):
    arr = np.array(lst)
    print(arr)
    print("Type of list now: ", type(arr))

x = ((1,2,3,4),(9,8,7,6))
y = [5,6,7,8]
print("Type of x: ", type(x))
tuple_to_arr(x)
print("Type of y: ", type(y))
list_to_arr(y)