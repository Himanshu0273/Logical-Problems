#Sort the string with proper word length

def true_alphabetic(str):
    # lst = str.split()
    # arr = []
    # for i in lst:
    #     arr.extend(list(i))
    # # print(sorted(arr))
    # arr = sorted(arr)
    arr =sorted([ch for ch in str if ch!=' '])
    c=0
    res=""
    for i in str:
        if i==" ":
            res+=" "
            continue
        res+=arr[c]
        c+=1
    
    print(res)
str = "have a nice day"

true_alphabetic(str)