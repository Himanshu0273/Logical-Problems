#Pair of socks
def pairs(lst):
    dic={}
    c=0
    for i in lst:
        dic[i] = dic.get(i, 0)+1
        # dic.update({i: dic[i]+1})   
        if dic[i]%2==0:
            c+=1
            dic[i]=0
    return c

n = int(input("Enter the length of the list: "))
lst = [int(input()) for _ in range(n)]
print(f"There are {pairs(lst)} pairs of socks")