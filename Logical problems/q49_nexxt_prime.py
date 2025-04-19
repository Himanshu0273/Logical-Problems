#Next Prime

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

def nextPrime(num):
    for i in range(num, 10000):
        if isPrime(i):
            return i


num = int(input("Enter a number: "))
print(nextPrime(num))