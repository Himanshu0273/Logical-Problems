#Expand String according to the digit before the character

def string_expansion1(str):
    res=""
    n = len(str)
    for i in range(n):
        if str[i].isdigit():
            if i!=n-1 and str[i+1].isalpha():
                x = int(str[i])
                res+=x*str[i+1]
                res=res[:-1]
                continue
        else:
            res+=str[i]
    return res


def string_expansion2(str):
    res=""
    x=0
    n=len(str)
    for i in range(n):
        if str[i].isdigit():
            x=int(str[i])
        
        else:
            res+=x*str[i]
            
    return res

str="3M123u42b12a"
print(string_expansion2(str))