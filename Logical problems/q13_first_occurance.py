#Find the first occurance of a pattern in a string, print -1 if not there
def first_occ(s, pat):
    print(f"The first occurance of \"{pat}\" in \"{s}\" is : {s.find(pat)}")
    
s = input("Enter the string: ")
pat = input("Enter the pattern: ")
first_occ(s, pat)