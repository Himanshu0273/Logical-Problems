#return a list of 2 numbers where first number is the sum of even numbers and second number is the sum of odd numbers of a given list

def listOfTwo(lst):
    e,o=0,0
    for i in lst:
        if i%2==0:
            e+=i
        else:
            o+=i
    
    return (e,o)

n=int(input("Enter the size of the list: "))
lst = [int(input()) for _ in range(n)]
print(listOfTwo(lst))