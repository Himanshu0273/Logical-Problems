#Perform operations like: Add, Subtract, multiple, divide on 2 pandas series


import pandas as pd

x1 = [2,4,6,8,10]
x2 = [1,3,5,7,9]

s1 = pd.Series(x1)
s2 = pd.Series(x2)

print("Addition:\n", s1+s2)
print("Subtraction:\n", s1-s2)
print("Multiplication:\n", s1*s2)
print("Division:\n", s1/s2)

# As lists: 
print("As List: Addition:", (s1+s2).to_list())
print("As List: Subtraction:", (s1-s2).to_list())
print("As List: Multiplication:", (s1*s2).to_list())
print("As List: Division:", (s1/s2).to_list())