# Write a Python program to convert a Panda module Series to Python list and it's type.

import pandas as pd


data = [1,2,3,4,5]
ser = pd.Series(data)

print(ser)
print(type(ser))
print()
print(ser.to_list())
print(type(ser.to_list()))
