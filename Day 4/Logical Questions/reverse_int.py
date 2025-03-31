#Reverse a number

def func(n):
    sign=1
    if n<0:
        sign=-1
        n*=-1
    
    rev=0
    d=0
    while n>0:
        d=n%10
        rev = (rev*10)+d
        n//=10    
        
    return rev*sign


n = int(input("Enter number to be reversed: "))
print("Reversed Number: ",func(n))
