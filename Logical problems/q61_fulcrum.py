#Find the fulcrum of the list
from functools import reduce
def fulcrum(lst):
    sum = reduce(lambda x,y:x+y, lst)
    ls=lst[0]
    for i in range(1, len(lst)-1):
        rs=sum-ls-lst[i]
        if rs==ls:
            return lst[i]
        ls+=lst[i]
    return -1

lst = [1, 2, 4, 9, 10, -10, -9, 3]
# lst=[8,8,8,8]
print(fulcrum(lst))