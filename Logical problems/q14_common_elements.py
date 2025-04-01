#Sum of the Common Elements in 3 lists

def common_list(lst1, lst2):
    lst=[]
    l1=lst1.copy()
    l2=lst2.copy()
    for i in l1:
        if i in l2:
            lst.append(i)
            lst2.remove(i)
    return lst
    

n = int(input("Enter the length of the lists: "))
print("Enter List 1 elements: ")
lst1 = [int(input()) for _ in range(n)]

print("Enter List 2 elements: ")
lst2 = [int(input()) for _ in range(n)]

print("Enter List 3 elements: ")
lst3 = [int(input()) for _ in range(n)]

lst_a = common_list(lst1, lst2)
lst_b = common_list(lst3, lst_a)
print("Sum of common elements in all the three lists are: ", (sum(lst_b)))