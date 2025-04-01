#Find a given number in a list in logarithmic time

def bin_search(lst, target):
    l,r=0, len(lst)-1
    while l<=r:
        mid = l+(r-l)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            l=mid+1
        else:
            r=mid-1
    
    return -1    

n = int(input("Enter the length of the array: "))

lst=[int(input()) for _ in range(n)]
lst.sort()
target = int(input("Enter the target number: "))

print(f"Target found at index: {bin_search(lst, target)}")