#Pair first with last, second with 2nd last, etc

def pairs(lst):
    res=list()
    size = len(lst)
    if size % 2 == 1:
        size+=1
    for i in range((size//2)):
        res.append([lst[i],lst[-i-1]])
        
    return res

lst = [5, 9, 8, 1, 2]
print(pairs(lst))