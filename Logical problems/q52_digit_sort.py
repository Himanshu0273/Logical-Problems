#Sort according to digit length

# def count_digit(n):
#     c=0
#     while n>0:
#         c+=1
#         n//=10
        
#     return c
       
    
# def digit_sort(lst):
#     lst = sorted(lst)

#     dig_len={}
#     for x in lst:
#         length = count_digit(x)
#         dig_len.setdefault(length, []).append(x)
        
#     sort_dict = dict(sorted(dig_len.items(), reverse=True))
#     res=[]
#     for x in sort_dict:
#         res.extend(sort_dict[x])
#     return res
# # lst = [int(input()) for _ in range (5)]

#M2:⭐⭐⭐

def count_digit(n):
    return len(str(n))


def digit_sort(lst):
    return sorted(lst, key=lambda x: (-count_digit(x),x))

lst = [1, 5, 9, 2, 789, 563, 444]
print(digit_sort(lst))