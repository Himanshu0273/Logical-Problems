#ARRAYS

#Question 1: Create array
print("Create Array")

import array as arr

a = arr.array('i' , [])

for _ in range(5):
    a.append(int(input("Enter Element: ")))
    
#Method 1
for i in a:
    print(i, end=" ")
    
#Method 2
print()
for i in range(len(a)):
    print(a[i], end=" ")
    
print()

#------------------------#

#Question 2: Reverse Array

import array as arr

print("Reverse the array")
n =int(input("Enter the length of the array: "))
a = arr.array('i', [])

for _ in range(n):
    x = int(input("Enter Element: "))
    a.append(x)
    
#Method 1: Using array slicing
rev_a = a[::-1]
print(rev_a)

#Method 2: Using reverse Function
a.reverse()
for i in range(n):
    print (a[i], end=" ")
    
print()

#------------------------#

#Question 3: Count frequency of the given element

import array as arr

print("Count frequency of the given element")
n = int(input("Enter Length of the array: "))

a = arr.array('i', [])

print("Enter elements in the array: ")
for _ in range(n):
    x = int(input())
    a.append(x)
    
target = int(input("Enter the number to be counted: "))

#Method 1
cnt = a.count(target)
print(f"{target} appears {cnt} times.")


#Method 2
freq=0
for i in range(n):
    if a[i] == target:
        freq+=1
    
print(f"{target} appears {freq} times.")

print()

#------------------------#

#Question 4: Remove the first occurance of the given element

import array as arr
print("Remove first occurance of the given element")
n = int(input("Enter length of the array: "))
a=arr.array('i', [])

for _ in range(n):
    x = int(input())
    a.append(x)
    
target = int(input("Enter number to remove: "))

#Using remove
a.remove(target)
print("Array with the first element Removed is: ")
for i in a:
    print (i, end=" ")

print()

#Using pop
a.pop(target)
print("Array with the first element Removed is: ")
for i in a:
    print (i, end=" ")
print()