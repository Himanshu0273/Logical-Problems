#Difference between the largest and the smallest combination of the letter

def diff(n):
    s = sorted(str(n))
    mini = int("".join(s))
    maxi = int("".join(s[::-1]))
    return maxi-mini

n = int(input("Enter a number: "))
print(diff(n))