lst = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(lst)

for i in range(n-1):
    min_ind = i
    for j in range(i+1,n):
        if lst[j]<lst[min_ind]:
            min_ind = j
        
    # min_val = lst.pop(min_ind)
    # lst.insert(i, min_val)
    lst[i],lst[min_ind] = lst[min_ind],lst[i]
        
print("Sorted List: ", lst)
            