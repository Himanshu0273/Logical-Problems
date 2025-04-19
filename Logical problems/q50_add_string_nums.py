#Add 2 numbers that are string

def sum_of_string(a, b):
    try:
        n = int(a)
        m = int(b)
        return n+m
    except ValueError:
        print ("Atleast one string contains a letter")
        return -1

a=input("Enter first string: ")
b=input("Enter second string: ")
print(sum_of_string(a,b))