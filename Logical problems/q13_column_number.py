#Column Number from the given column name 

def col_num(s):
    
    # M1:
    # dic = {chr(ord('A') + x): x + 1 for x in range(26)}

    # c=0
    # for i in s:
    #     c = c*26+dic[i]
        
    # print (c)

    #M2:
    res=0
    for ch in s:
        res = res*26+(ord(ch)-ord('A')+1)
        
    print(res)

s = input("Enter column name: ").upper()
col_num(s)