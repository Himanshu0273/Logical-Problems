# Check if Perfect Square

import math

def perfect_sq(n):
    for i in range(math.isqrt(n)+1): #math.isquare(n): Gives the int value of the square root of a number instead of the normal float type return
        if (i*i) == n:
            print(f"It is the Perfect Square of {i} !!")
            break

    else:
        print("Not a Perfect Square")
        
n = int(input("Enter the number: "))

perfect_sq(n)