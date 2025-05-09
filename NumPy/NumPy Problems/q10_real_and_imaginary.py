# Separate real and imaginary parts of a complex number

import numpy as np

def func(arr):
    real = np.real(arr)
    imaginary = np.imag(arr)
    print("Real Parts: ", real)
    print("Imaginary Parts: ", imaginary)

x = [1.00000+0.j, 2.21124+0.707070j]
arr = np.array(x, dtype=complex)
func(arr)