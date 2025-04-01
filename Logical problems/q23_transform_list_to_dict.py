#Transform string to list of dictionaries

def to_dict(lst):
    res=[]
    for i in lst:
        dic={}  
        dic[i] = ord(i)
        res.append(dic)
        
    return res
n=int(input("Enter length of the list: "))
lst = [input()  for _ in range(n)]
print(to_dict(lst))
