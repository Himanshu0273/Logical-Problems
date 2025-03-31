#Find the first occurance of a pattern in a string, print -1 if not there

s = input("Enter the string: ")
pat = input("Enter the pattern: ")
print(f"The first occurance of \"{pat}\" in \"{s}\" is : {s.find(pat)}")