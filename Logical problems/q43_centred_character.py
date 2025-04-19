#Character is in the centre or not

def centered_char(s):
    l = len(s)
    c=0
    for i in s:
        if i==' ':
            c+=1
        else:
            break
    
    print("Total Length: ",l)
    print("Spaces before the character: ",c)
    print(True if ((l-c-1)==c) else False)
    

s=input("Enter the string: ")
centered_char(s)