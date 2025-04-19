#Count digits:

def count_digits(n):
    c=0
    while n>0:
        c+=1
        n//=10
    return c

n=input("Enter number: ")
# if 'e' in n:
x = n.find('e')
if x!=-1:
    num = float(n[:x])
    expo = int(n[x+1])
    num = num*(10**expo)
else:
    num = int(n)
print(count_digits(int(num)))