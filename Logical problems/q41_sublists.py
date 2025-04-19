#Sublists containing the same elements:


nums=[1,5,3,4,1,2,3,5,6,3,4,5,2,3,4,5]
# nums=['a','b','c','b','c','a']\
freq = dict()
for i in nums:
    freq[i] = freq.get(i, 0)+1

res=[[i]*j for i,j in freq.items()]
# for i,j in freq.items():
#     lst = [i for _ in range(j)]
#     res.append(lst)
print(res)