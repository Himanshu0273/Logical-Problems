#All permutations of a string using string and iterative approach

def iterative(s):
    lst = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            str = s[i:j+1]
            print(str)
            lst.append(str)
            
    print ()
    return lst
    
def recursive(s,lst, start=0, end=0):
    if len(s)==start:
        return
    
    elif len(s)==end:
        recursive(s,lst,start+1,start+1)
    
    else:
        print(s[start:end+1])
        lst.append(s[start:end+1])
        recursive(s,lst,start,end+1)
    
    return lst
s = "abcdefg"
lst1 = iterative(s)
lst2 = recursive(s,[],0,0)
if lst1==lst2:
    print("Both gave same results!!")
    
else:
    print("Both methods gave different results!!")