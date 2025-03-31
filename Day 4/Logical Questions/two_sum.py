#Two Sum:

def two_sum(lst, target):
    d={}
    for i in range(len(lst)):
        comp = target-lst[i]
        if comp in d:
            return (d[comp], i)
            break
        else:
            d[lst[i]] = i
    return {-1,-1}

n = int(input("Length of array: "))
target=int(input("Enter the target value: "))
lst=[int(input()) for x in range(n)]

        
print(two_sum(lst, target))