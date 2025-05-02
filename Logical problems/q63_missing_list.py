#Return length of the missing list

def find_missing(arr):
    arr = sorted(arr)
    c=1
    for i in arr:
       n = len(i)
       if c==n:
           c+=1
       else:
           return c 
       
def pythonic_way(arr):
    arr = sorted(arr)
    lengths = set(len(x) for x in arr)
    actual = set([i for i in range(1, len(arr[-1])+1)])
    print("Missing Length is: ", (actual-lengths).pop())
    
arr =[[4, 4, 4, 4], [1], [3, 3, 3]]
print(find_missing(arr))
pythonic_way(arr)