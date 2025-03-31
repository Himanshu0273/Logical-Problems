def max_freq(lst):
    d=dict()
    # maxi=0, me=lst[0]
    for x in lst:
        d[x] = d.get(x, 0) + 1
    return max(d, key=d.get                                        )
n = int(input("Enter length of the array: "))
lst = [int(input()) for _ in range(n)]
print("Majority Element in the array is: ", max_freq(lst))
