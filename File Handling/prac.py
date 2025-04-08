# from functools import reduce

# nums=[1,2,3,4,5,6,7,8]
# squared = list(map(lambda x: x**2, nums))
# print(squared)

# # evens = list(x for x in nums if x%2==0)
# evens = list(filter(lambda x: x%2==0, nums))
# print (evens)

# sum = reduce(lambda x,y: x/y, nums)
# print(sum)


from collections import Counter
lst = ['apple', 'banana', 'apple', 'banana', 'banana', 'orange']
dic = dict(Counter(lst))
print(dic)