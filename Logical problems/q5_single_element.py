#Single Element

# The freq way is:
#dic = {}
# This is the way to increase freq.
# d[num] = d.get(num, 0)

def func(lst):
    d=[]
    for x in lst:
        if x not in d:
            d.append(x)
        else:
            d.remove(x)
    
    return d[0]

n = int(input("Enter the length of the list: "))
lst = [int(input("Enter element: ")) for _ in range(n)]

print("Only single element: ", func(lst))