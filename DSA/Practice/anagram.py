# # An Anagram Detection Example
# # a. Desc -> One string is an anagram of another if the second is simply a
# # rearrangement of the first. For example, 'heart' and 'earth' are anagrams...
# # b. I/P -> Take 2 Strings as Input such abcd and dcba and Check for Anagrams
# # c. O/P -> The Two Strings are Anagram or not....
# # 7. Take a range of 0 - 1000 Numbers and find the Prime numbers in that range.
# # 8. Extend the above program to find the prime numbers that are Anagram and
# # Palindrome
# from math import sqrt

# def anagram(s,t):
#     s= ''.join(sorted(s))
#     t= ''.join(sorted(t))
#     return s==t
    
# def prime():
#     lst=[]
#     for i in range(1,1001):
#         if i%2==0:
#             continue
#         for j in range(3, (sqrt(i)+1)):
#             if i%j==0:
#                 break
#         else:
#             lst.append(i)
    
# s = "dcba"
# t = "abcd"
# print(anagram(s,t))