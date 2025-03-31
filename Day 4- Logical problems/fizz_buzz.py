#FizzBuzz Numbers

n = int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print("FizzBuzz")
elif n%3!=0 and n%5!=0:
    print("Not divisible by 3 or 5")
else:
    print("Fizz" if n%3==0 else "Buzz")