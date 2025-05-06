#Create the stair case pattern using # and _

def positive_size(n):
    for i in range(n):
        for j in range(n-i-1):
            print("_",end="")
        for k in range(n-i-1, n):
            print("#", end="")
        print()

def negative_size(n):
    for i in range(n):
        for j in range(n-i):
            print("#",end="")
        for k in range(n-i-1, n-1):
            print("_", end="")
        print()


n = 8
m = -8
if n>0:
    positive_size(n)
else:
    negative_size(abs(m))