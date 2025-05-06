#Find the cup the ball ends in

def cup_swaps(lst):
    pos='B'
    for i in lst:
        if i[0]==pos:
            pos=i[1]
        elif i[1]==pos:
            pos=i[0]
    return pos

lst=["BA", "AC", "CA", "BC"]
print(cup_swaps(lst))