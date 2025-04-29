#Matrix Multiplication
import numpy as np

def matrix_multiplication(m1, m2):
    print(np.dot(m1,m2))
    
x = [[12,7,3],[4,5,6],[7,8,9]]
y = [[5,8,1],[6,7,3],[4,5,9]]

m1 = np.array(x)
m2 = np.array(y)
matrix_multiplication(m1,m2)