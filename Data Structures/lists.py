#Question 1: Sum of elements
a = [1,2,3,4,5]
print(f"Sum of all elements in the list is: {sum(a)}")

#------------------------#

#Q2: Product of all elements
import math

a = [1,2,3,4,5]
print(math.prod(a))

#------------------------#

#Q3: Find minimum
a = [6,4,7,8,3,9]
print (min(a))

#------------------------#

#Q4: Count the strings with len>2 and have the same first and last letter
c=0
lst = ['abc', 'xyz', 'aba', '1221']

for i in lst:
    if len(i)>2 and i[0]==i[-1]:
        c+=1

print(c)

#------------------------#

#Q5: Sort a list according to the last element of the tuple
a = [(2,5,4), (1,2,3), (4,4,1), (2,3,5), (2,1,2)]
sorted_a = sorted(a, key=lambda x:x[-1])
print(sorted_a)

#------------------------#

#Q6: Remove Duplicates

a = [1,1,3,2,3,1,4,5,3,2,4,5,1]

#Using Loops: Order Maintained, but slowest
unique=[]
for i in a:
    if i not in unique:
        unique.append(i)
        
print(unique)

#Using set: Order not maintained, but fastest
# print(a)
# a = list(set(a))

#------------------------#

#Q7: Clone or copy a list

a=[1,2,'a',4.5]

#using copy:
b=a.copy()
print(b)

#Using list:
c = list(a)
print(c)

#Using slice function
d = a[:]
print(d)

#------------------------#

#Q8: Select elements from a list with length greater than n and append them in a new list

lst =['hi', 'apple', 'hel', 'helo']
n =int(input("Enter the desired length of strings: "))
res=[]
for i in lst:
    if len(i)>n:
        res.append(i)
        
print(res)

#------------------------#

# Q9: At lest one memeber common
lst1 = ["Hi", "hello", "Welcome"]
lst2 = ["New", "Hi", "Lists"]

for i in lst1:
    if i in lst2:
        print("True")
        break
    else:
        print("False")
        break
    
#------------------------#

#Q10: Remove 0th, 4th, 5th element
lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

a=[5,4,0]
for i in a:
    lst.pop(i)
    
print(lst)

#------------------------#

#Q11: generate all possible permutations of a list
from itertools import permutations

n=int(input())
a = [int(input()) for i in range(n)]

print(list(permutations(a)))

#------------------------#

#Q12: Difference between 2 lists

from collections import Counter

a = [1,2,3,4]
b = [3,4,5,6,7,8]

#Method 1:
c1 = Counter(a)
c2 = Counter(b)
c=c1-c2
print(list(c.elements()))

#Method 2:
# lst = [item for item in a if item not in b]
# print(lst)

#------------------------#

#Q13: Append one list to another
lst1 = [1,2,3]
lst2 = ['Hi',4,5]

# for i in lst2:
#     lst1.append(i)
# print(lst1)

lst1.extend(lst2)
print(lst1)

#------------------------#

#Q14: Circularly similar
lst1 = [1,2,3,4]
lst2 = [3,4,1,2]

# Method 1:
c=0
for i in range(len(lst1)):
    if(lst1==lst2):
        print ("The are circularly Similar!!")
        c=1
        break
    x = lst1[0]
    lst1.pop(0)
    lst1.append(x)

if c==0: 
    print("Not Same!!")    

#------------------------#

#Q15: Common elements
lst1 = [1,2,6,5]
lst2 = [3,4,1,2]


#Method 1:
# res=[]
# for i in lst2:
#     if i in lst1:
#         res.append(i)
        
#Method 2: Using sets
res=[x for x in lst1 if x in lst2]

    
print (res)

#------------------------#


#Q16: Split based on first character

from collections import defaultdict

def split_by_first_char(words):
    grouped_words = defaultdict(list)
    [grouped_words[word[0].lower()].append(word) for word in words]
    return dict(grouped_words)

words_list = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado", "carrot"]
res = split_by_first_char(words_list)

for key, val in res.items():
    print(f"{key}: {val}")

#------------------------#

#Q17: Remove duplicate lists from list

lst = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

#Method 1: Using set
# res=list(set())

# for i in lst:
#     if i not in res:
#         res.append(i)
        
res = list(map(list, {tuple(sublst) for sublst in lst}))
print(res)
