#Question 1: Creating a tuple

# t = (0,1,2)
# t = 'a','b','c'
t = tuple([3,4,5])
print(t)

#------------------------#

#Question 2: Create tuple with multiple types
t = 1,'a',4,'b',5,5
print(t)

#------------------------#

#Question 3: Unpacking Tuples

t = (1,2,3,4)

#Basic Unpacking
a,b,c,d = t
print(a,b,c,d)

#Unpacking using *
a,*b,c = t
print(a,b,c)

#Nested unpacking
t = 1,(2,3),4
# a,(b,c),d = t
a,b,c=t
print(a,b,c)

#Ignoring using _
t = (1,2,3,4,5)
a,_,_,_,b = t
print(a,b)

#------------------------#

#Question 4: Cloning a Tuple?

t = (1,2,3,4)

#Using Slicing
copy_tuple = t[:]
print(copy_tuple)

#Using tuple() Constructor
clone = tuple(t)
print(clone)

import copy
#Using copy() for nested tuple with list
t2 = (1,[2,3],4)
clone = copy.deepcopy(t2)
print(clone)

#------------------------#

#Question 5: Remove repeating elements
t=(1,2,3,5,2,5,3,3,6,8,5)

#M1: converting to set and then to tuple: Does not preserve order
st=tuple(set(t))
print(st)

#M2: using dict.fromkeys(t): Preserves order
dt = tuple(dict.fromkeys(t))
print(dt)

#------------------------#

# Question 6: Does an element exist in the tuple

t = (2,4,3,1,5,5,3,8,5,1,9)
target = 9
print(target in t)

#------------------------#

# Question 7: List to tuple
l = [1,2,"A",4.5]
print(type(l))
l=tuple(l)
print(type(l))

#------------------------#

#Question 8: Remove an item
t = (10,20,30,40,50)
print(t)
target = 10

t=list(t)
t.remove(target)
t=tuple(t)
print(t)

#------------------------#

# Question 9: Slice a tuple
t = (1,2,3,4)
print(t[:])
print(t[1:3])
print(t[:3])
print(t[1:])
print(t[-3:-2])
print(t[-2:])

#------------------------#

#Question 10: Reverse

t=(1,2,3,4)

#M1: Slicing
print(t[::-1])

#M2: reveresed(t)
t = tuple(reversed(t))
print(t)

#M3: Loop:
t = tuple(x for x in reversed(t))
print(t)