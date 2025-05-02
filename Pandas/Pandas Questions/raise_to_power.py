#Raise all elements to the power of 3 in a series

import pandas as pd

x = [0,1,2,3,4,5,6]
ser = pd.Series(x)
print(ser)
print()
print((ser**3).to_list())