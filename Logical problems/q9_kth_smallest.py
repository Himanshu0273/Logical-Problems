#kth smallest element

def kth_smallest(lst, k):
    lst.sort(reverse=True) #In-place sorting
    while k>1:
        lst.pop()
        x=lst[-1]
        k-=1
    print(x)
n = int(input("Enter the length of the list: "))
lst = [int(input()) for _ in range(n)]
k = int(input("Enter the k value for the kth smallest integer: "))
# lst = sorted(lst,reverse=True) #: Returns a new list, 

# lst=set(lst)# if the kth smallest among the distinct values of the list, use a set 

kth_smallest(lst, k)
