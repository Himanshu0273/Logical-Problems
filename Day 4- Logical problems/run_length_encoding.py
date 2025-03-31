#Run-length Encoding

def encode(s):
    c=0
    ch=s[0]
    res=""

    for i in s:
        if i==ch:
            c+=1
        else:
            res+= str(c) + ch
            ch=i
            c=1
    res+=str(c)+ch
    return res

def decode(s):
    c=0
    res=""
    for i in s:
        if i.isalpha():
            res+=(i*c)
            c=0
        else:
            c = (c*10)+int(i) 
    
    res+=(s[len(s)-1]*c)
    return res

s = input("Enter the string: ")
t=s
print("Encoded form is: ",encode(s))
s1=encode(s)
print("Decode string: ", decode(s1))

print("Properly done" if t==decode(s1) else "No")    