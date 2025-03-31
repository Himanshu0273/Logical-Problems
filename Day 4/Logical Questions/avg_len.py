def remove_punc(s):
    lst = []
    
    return lst

def avg_len(s):
    lst = remove_punc(s)
    s=0
    n = len(lst)
    for i in lst:
        s+=len(i)    
    return s/n
        
    
s = input("Enter the length: ")
print("Average length of words: ", avg_len(s))
