import numpy as np

x = [[1,2,3],[4,5,6],[7,8,9]]
arr = np.array(x, np.int64)

print("Vertical Sum: ",arr.sum(axis=0))
print("Horizontal Sum:", arr.sum(axis=1))

#Transpose
print (arr.T)


#Returns a flat iterator
for a in arr.flat:
    print(a)
print()
#Returns the dimensions of the array created
print("Dimensions: ",arr.ndim)

#Returns the size of the array
print("Size: ",arr.size)

#Returns the number of bytes being used by the array
print("Bytes: ", arr.nbytes)