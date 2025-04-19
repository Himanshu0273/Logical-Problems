#Find factorial of factorial

def fact(n):
    if(n==1):
        return n
    return n*fact(n-1)

def fact_of_fact(n):
    if n==1:
        return n
    return fact(n)*fact_of_fact(n-1)

n=int(input("Enter a number: "))
print(fact_of_fact(n))