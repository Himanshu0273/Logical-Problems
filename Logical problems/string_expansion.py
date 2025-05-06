#Expand String according to the digit before the character

def string_expansion(str):
    res=""
    for i in range(len(str)-1):
        if str[i] in "123456789":
            if str[i].isalpha():
                x = int(str[i])
                print(type(x))
                for i in range(x):
                    res+=str[i+1]
                print(str[i])
                continue
            else:
                continue
        res+=str[i]
    
    if str[len(str)-1] not in "123456789":
        res+=str[len(str)-1]
    return res

str="3Mat"
print(string_expansion(str))