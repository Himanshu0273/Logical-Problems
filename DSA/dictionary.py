#Question 1: Sort dictionary according to values:

dict1 = {
    "a": 6,
    "b": 7,
    "c": 4    
}

d = dict(sorted(dict1.items(), key=lambda items: items[1], reverse=True))
print("Descending Order:", d)

d = dict(sorted(dict1.items(), key=lambda items: items[1]))
print("Ascending Order:", d)

#------------------------#

#Question 2: Add a key to the Dictionary
dict1 = {
    "a": 6,
    "b": 7,
    "c": 4    
}

print("Original Dict", dict1)

# dict1["d"] = "New_val"
dict1.update({"e":10})
print("Updated dict", dict1)

#------------------------#

#Question 3: Concatenate multiple dicts
import collections

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

#using |
d = dic1 | dic2 | dic3
print(d)

#Using ChainMap from Collection
dt = dict(collections.ChainMap(dic3, dic2, dic1))
print(dt)

#Using .update()
d =dic1.copy()
d.update(dic2)
d.update(dic3)
print(d)

#------------------------#

#Question 4: Looping through a dict

dict1 = {
    'a': 1, 
    'b': 2, 
    'c': 3
}

for x in dict1:
    print(f"{x} : {dict1[x]}")
    
#------------------------#
#Question 5: Create a list with i:i*i

#For loop
d = {}

n=5
for i in range(1,n+1):
    d.update({i: (i*i)})
    
print(d)

#Dict comprehension
n=5
d={x: x*x for x in range(1,n+1)}
print (d)

#------------------------#

#Question 6: Remove a key from a dictionary
dict1 = {
    'a': 1,
    'b': 2,
    'c': 3,
}

dict1.pop('a')
print(dict1)

del dict1['b']
print(dict1)

#------------------------#

#Question 7: Print all unique values from a list of dictionaries

dict1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

unique = set()

for x in dict1:
    for val in x.values():
        unique.add(val)

print(unique)

#------------------------#

#Question 8: 

str = "Hi Himanshu"
freq=dict()

for i in str:
    if i in freq:
        freq.update({i:freq[i]+1})
    else:
        # freq.update({i:1})
        freq[i] = 1
        
print(freq)

#------------------------#

#Question 9: Table Format

dict1 = {
    1: ["Samuel", 21, 'Data Structures'], 
    2: ["Richie", 20, 'Machine Learning'], 
    3: ["Lauren", 21, 'OOPS with java'], 
}

#Method 1
# for i in dict1:
#     print (i.format(), end="\t")
    
# print()
# for i in dict1:
#     for x in dict1[i]:
#         print (x, end="\t")
#     print() 

#Method 2

print("{:>10} {:>10} {:>20}".format("NAME", "AGE", "COURSE")) 

for k,v in dict1.items():
    name, age, course = v
    print("{:>10} {:>10} {:>20}".format(name, age, course)) 
    
#------------------------#

# Question 10: Count how many times a key has a certain value in a list of dictionaries

dict1 = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

#Method 1: Using Loops
c=0
for x in dict1:
    if x['success'] == True:
        c+=1

print(c)   

#Method 2: Dictionary Comprehension
s = sum(1  for x in dict1 if x['success']==True)  
print(s)
   
s1 = sum(x['success'] for x in dict1)
print(s1)

#------------------------#

#Question 11: List items as Dictionary Keys

lst = ['a','b','c','d']

dic = dict.fromkeys(lst)
print(dic)

#------------------------#

#Question 12:

dic = {
    'a': 1,
    'b': 2,
    'c': 3,
}

if len(dic)>1:
    print("Multiple keys found")
else:
    print(False)
    
#------------------------#

#Question 13: Count values in a dictionary that are a list
dict = {
    'a': [1,2,3,4],
    'b': 12,
    'c': [5,6,7,8],
    'd': 4.5
}


c=0
for x in dict:
    if isinstance(dict[x], list):
        c+=1
        
print(c)