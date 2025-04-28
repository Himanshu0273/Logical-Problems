import numpy as np

x = [4,3,65,1,2,8]
y = [[1,2,3],[4,5,6],[7,1,0]]

ar1 = np.array(x)
ar2 = np.array(y)
print("1D Array: ", ar1)
print("2D Array:\n", ar2)

print("Max in index in 1D: ", ar1.argmax())
print("Min in index in 1D: ", ar1.argmin())
print("Max in index in 2D: ", ar2.argmax())
print("Min in index in 2D: ", ar2.argmin())
print("Maximum in each col: ", ar2.argmax(axis=0))
print("Minimum in each col: ", ar2.argmin(axis=0))
print("Maximum in each row: ", ar2.argmax(axis=1))
print("Minimum in each row: ", ar2.argmin(axis=1))
print("Sorted for each col:\n", ar2.argsort(axis=0))
print("Sorted for each row:\n", ar2.argsort(axis=1))