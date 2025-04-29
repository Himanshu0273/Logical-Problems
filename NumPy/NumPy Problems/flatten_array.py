import numpy as np

a = np.array([[1,2,3],[4,5,6]])
# a = np.flat(a)
print(a.reshape(1,-1))

# for x in a.flat:
#     print(x)