#Last digit of c = last_digit(a)*last_digit(b)

def last_digit(a,b,c):
    last_a = a%10
    last_b = b%10
    last_c = c%10
    s = a*b
    last_s = s%10
    return last_s == last_c


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print(last_digit(a,b,c))