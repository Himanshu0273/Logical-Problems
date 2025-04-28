import numpy as np

x = [[1,2,3],[4,5,6],[1,2,1]]
y = [[1,4,5],[3,4,5],[7,8,1]]
z = [[1,4,5],[3,4,5]]
ar = np.array(x)
ar2= np.array(y)
ar3= np.array(z)
autoar = ar3.reshape(2,-1)
print(ar+ar2)
print(ar*ar2)
print(ar-ar2)

print(autoar)