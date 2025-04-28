import numpy as np

#Conversion from other python structures
myarr = np.array([[1,2,3,4],[2,1,2,3]], np.int64)
print(myarr)
print(myarr.shape)
print(myarr.dtype)
myarr[0,3] = 5
print(myarr)


#Intrinsic numpy array creation  
zeroes = np.zeros(2)
print("1st Zeroes: ")
print(zeroes)
zeroes = np.zeros((2,5))
print("2nd Zeroes: ")
print(zeroes)

rng = np.arange(12)
print(rng)

ls = np.linspace(1,5, 10)
print(ls)

emp = np.empty(20)
print(emp)

ide = np.identity(10)
print(ide)


# x = [[1,2,3],[4,5,6],[7,8,9]]
arr = np.arange(99)
print(arr)
arr = arr.reshape(3,33)
print(arr.shape)
print(arr)
arr = arr.ravel()
print(arr.shape)
print(arr)


