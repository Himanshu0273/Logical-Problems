# Select the character with the maximum occurance
from collections import Counter

def max_occur(str):
    freq = Counter(str)
    print(freq)
    res=[]
    maxi=max(freq.values())
    print(maxi)
    for i,j in freq.items():
        if j==maxi:
            res.append(i)
        
    return res

str = "Computer Science"
# str="system admin"
print(max_occur(str))