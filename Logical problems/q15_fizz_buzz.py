#FizzBuzz Numbers
def fizz_buzz(n):
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%3!=0 and n%5!=0:
        print("Not divisible by 3 or 5")
    else:
        print("Fizz" if n%3==0 else "Buzz")
    
n = int(input("Enter a number: "))
fizz_buzz(n)