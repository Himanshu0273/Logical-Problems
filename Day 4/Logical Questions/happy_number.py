def happy_num(n):
    # d=0
    # while n!=0:
    #     x=n%10
    #     d+=x**2
    #     n//=10
    # print(d)                
    # return d 
    return sum(int(digit)**2 for digit in str(n))
    

n=int(input("Enter a number: "))
# if(happy(n)):
#     print("Happy Number")
    
# else:
#     print("Not Happy Number")
seen = set()
    
while n!=1 and n not in seen:
    seen.add(n)
    n=happy_num(n)
    
print("Happy Number!!" if n==1 else "Not Happy Number!")