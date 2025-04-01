#Dice rolls
import random

def dice_game(lst):
    c=0
    print("The three rolls are: ", lst)
    for t in lst:
        if t[0] == t[1]:
            return 0
        else:
            c += (t[0]+t[1])
    return c

lst=[]
for _ in range(3):
    a = random.randint(1,6)
    b = random.randint(1,6)
    t = a,b
    lst.append(t)

print("Your total is: ", dice_game(lst))