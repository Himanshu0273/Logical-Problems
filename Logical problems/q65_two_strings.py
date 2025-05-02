#Perform set operations on 2 strings

def set_func(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    print("Common unique letters: ", ''.join(sorted(s1&s2)))
    print("Unique letters in String 1: ", ''.join(sorted(s1-s2)))
    print("Unique letters in String 1: ", ''.join(sorted(s2-s1)))

s1 = "happiness"
s2 = "envelope"
set_func(s1,s2)