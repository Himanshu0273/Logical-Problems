#Check if the given word is alphabetically sorted or not
def func(word):
    for i in range(len(word)-1):
        if word[i]>word[i+1]:
            return False
    return True

def is_alphabetically_sorted(s):
    lst = s.split()
    for i in lst:
        if len(i)>2 and func(i):
            return True    
        
    return False

s = "The biopsy returned negative results."
print(is_alphabetically_sorted(s))