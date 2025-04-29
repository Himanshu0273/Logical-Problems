#Matrix Multiplication
import numpy as np

def matrix_multiplication(m1, m2):
    print(np.dot(m1,m2))
    
x = [[5,1,3],[1,1,1],[1,2,1]]
y = [1,2,3]

m1 = np.array(x)
m2 = np.array(y)
matrix_multiplication(m1,m2)