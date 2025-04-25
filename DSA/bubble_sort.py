lst = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(lst)

for i in range(n-1):
    for j in range(n-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
            
print("Sorted List: ", lst)