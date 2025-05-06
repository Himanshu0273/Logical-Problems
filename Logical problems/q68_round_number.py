#Round the number to the nearest divisible number

def round_number(num, n):
    if num%n==0:
        return 
    x = num//n
    a = n*x
    b = n*(x+1)
    if abs(num-a) == abs(num-b):
        return max(a,b)
    return a if (abs(num-a))<abs(num-b) else b
    


num=33
n=35
print(round_number(num,n))