#Sort positive numbers:

def func(lst):
    if len(lst)==0:
        return []
    lst1 = [x for x in lst if x>0]
    lst1.sort()
    i=0
    for j in range(len(lst)):
        if lst[j]>0:
            lst[j] = lst1[i]
            i+=1
    return lst

n = int(input("Enter the length of array: "))
lst= [int(input()) for x in range(n)]
print(func(lst))