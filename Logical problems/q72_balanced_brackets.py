#Balance the brackets
# from collections import deque

def split_brackets(str):
    temp=""
    res=[]
    c=0
    n=len(str)
    for i in range(n):
        if str[i] == "(":
            temp+=str[i]
            c+=1
        elif str[i]==')':
            temp+=str[i]
            c-=1
            if c==0:
                res.append(temp)
                temp=""
                
    return res

str = "((()))(())()()(()())"
# str="((()))"
print(split_brackets(str))