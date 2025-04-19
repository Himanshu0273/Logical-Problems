#Sort by letter

def sort_by_letter(lst):
    # my_dict = dict()
    # for i in lst:
    #     for ch in i:
    #         if ch.isalpha():
    #             my_dict[ch] = i
    #             break
           
    # sorted_dict = sorted(my_dict.items())
    # res = [x[1] for x in sorted_dict]
    res = sorted(lst, key=lambda x: next(c for c in x if c.isalpha()))
    print(res)

lst = ["932c", "832u32", "2344b"]
# lst = ["99a", "78b", "c2345", "11d"]
sort_by_letter(lst)