def rev_lst(lst):
    # l=0
    # r=len(lst)-1
    l,r = 0, len(lst)-1
    while l<=r:
        lst[l], lst[r] = lst[r], lst[l]
        l+=1
        r-=1
    
    return lst

n = int(input("Enter the length of the list: "))
lst = [int(input()) for _ in range(n)]

print(rev_lst(lst))