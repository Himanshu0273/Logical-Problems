lst = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(lst)

for i in range(1, n):
    key = lst[i]
    j=i-1
    while j>=0 and lst[j]>key:
        lst[j+1]=lst[j] 
        j-=1
    lst[j+1] = key
    
print("Sorted List: ", lst)