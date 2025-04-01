#Reverse only the vowels in a string
def rev_vowels(s):
    s=s.lower()
    vow=[ch for ch in s if ch in "aeiou"]
    res=""
    for i in range(len(s)):
        if s[i] in "aeiou":
            res+=vow[len(vow)-i]
            # vow.pop()
        else:
            res+=s[i]
    return res

s = input("Enter the string: ")
    
print(f"The string with vowels reversed is: {rev_vowels(s)}") 