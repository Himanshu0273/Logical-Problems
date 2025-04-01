#Missing letters:

#M1: Brute force
# def get_missing_letters(s):
#     s=s.lower()
#     res=""
#     for i in "abcdefghijklmnopqrstuvwxyz":
#         if i not in s:
#             res+=i
    
#     return res

import string
#M2: Pythonic Way:
def get_missing_letters(s):
    letters = set(string.ascii_lowercase)
    present = set(s)
    missing = sorted(letters-present)
    return (''.join(missing))
s = input("Enter your string: ")
print(f"The missing letters are: {get_missing_letters(s)}")