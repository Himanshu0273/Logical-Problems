def bin_search(lst, target):
    low = 0
    high = len(lst)-1
    while low<=high:
        mid = (low+high)//2
        if lst[mid] == target:
            return mid
        elif lst[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return -1    
lst = [1,2,3,4,5,6,7,8,9]
print(bin_search(lst, 9))
