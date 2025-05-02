# Write a Python program to create and display a one-dimensional array-like object
# containing an array of data using Pandas module.

import pandas as pd

data = [1,2,3,4,5,6]
ser = pd.Series(data)
print(ser)
print(type(ser))