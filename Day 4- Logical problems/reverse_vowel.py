#Reverse only the vowels in a string
def rev_vowels(s):
    s=s.lower()
    vow=[x for x in s if x in "aeiou"]
    res=""
    for i in s:
        if i in "aeiou":
            res+=vow[len(vow)-1]
            vow.pop()
        else:
            res+=i
    return res

s = input("Enter the string: ")
    
print(f"The string with vowels reversed is: {rev_vowels(s)}") 