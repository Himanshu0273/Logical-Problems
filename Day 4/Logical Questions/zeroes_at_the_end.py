# def func(lst):
#     lst1=[]
#     cnt=0
#     for i in range(len(lst)):
#         if lst[i]!=0:
#             lst1.append(lst[i])
#         else:
#             cnt+=1
            
#     while cnt>0:
#         lst1.append(0)
#         cnt-=1
        
#     return lst1


def func(lst):
    l=0
    r=0
    while r in range(len(lst)):
        if lst[r]!=0:
            lst[l], lst[r] = lst[r], lst[l]
            l+=1 
        r+=1
    
    return lst 
n = int(input("Enter length of the list: "))
lst=[int(input("Enter Element: ")) for _ in range(n)]

print(func(lst))