#Question 1: Create a set

st = {1,2,3,4,5,7,4,3}
print(st)

#Using set() Constructor
st1 = set([2,1,3,2,1,3,5,6,7])
print(st1)

#------------------------#

#Question 2: iterate over set

st = {1,2,3,4,2,1}
for x in st:
    print(x, end=" ")
    
print()
print (set(x for x in st))

#------------------------#

#Question 3:add members in a set
st = {1,2,3,4,5}
print("Old: ",st)

st.add(10)
print("New: ",st)

s1 = {"a",'b','b'}
st.update(s1)
print("New: ",st)

#------------------------#

#Question 4: Remove items from set

st = {1,2,3,4,5}
print("Old: ",st)

st.add(10)
print("New: ",st)

s1 = {"a",'b','b'}
st.update(s1)
print("New: ",st)

#remove()
st.remove(5)
print("Remove: ", st)

#discard()
st.discard(2)
print("Discard: ", st)
#pop()
st.pop()
print("Pop: ", st)

#clear
st.clear()
print(st)

#del: cannot even access st
del st
# print(st) This will now throw error

#------------------------#

#Question 5: Remove item if present
st = {1,2,3,4,5}
print("Old: ",st)

target = 4

#Using Remove
# if target in st:
#     st.remove(target)
#     print(st)
    
#Using Discard
st.discard(target)
print(st)

#------------------------#

#Question 6: Intersection of sets:

st1 = {1,2,3,4,5}
st2 = {4,5,6,7,8}

#Intersection:
st3 = st1 & st2
st4 = st1.intersection(st2)
print(st3)
print(st4)

#Intersection update:
st1.intersection_update(st2)
print(st1)


#------------------------#

#Question 7: Union of sets:

st1 = {1,2,3,4,5}
st2 = {4,5,6,7,8}

#Union:
st3 = st1 | st2
st4 = st1.union(st2)
print(st3)
print(st4)

#union update:
st1.update(st2)
print(st1)

#------------------------#

#Question 8:Difference of sets:
st1 = {1,2,3,4,5}
st2 = {4,5,6,7,8}

#Union:
st3 = st1 - st2
st4 = st1.difference(st2)
print(st3)
print(st4)

#union update:
st1.difference_update(st2)
print(st1)

#------------------------#

#Question 9:Symmetric Difference

st1 = {1,2,3,4,5}
st2 = {4,5,6,7,8}

#Union:
st3 = st1 ^ st2
st4 = st1.symmetric_difference(st2)
print(st3)
print(st4)

#union update:
st1.symmetric_difference_update(st2)
print(st1)

#------------------------#

#Question 10:Clear a set:
st1 = {1,2,3,4,5}

    
st1.clear()
print(st1)

#------------------------#

#Question 11:
fs = frozenset([1,2,3,4])

print(fs)

st = {3,4,5,6}
print("Union: ", fs|st)
print("Intersection: ", fs&st)
print("Difference: ", fs-st)

print(fs)
#------------------------#

#Question 12: Max and Min elements in a set

st1 = {4,3,5,2,6,9}
print("Min element in set is: ",min(st1))
print("Max element in set is: ",max(st1))
