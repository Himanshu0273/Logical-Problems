#Find the table upto k for a given number

def table_of_n(n,k):
    return [n*(i+1) for i in range(k)]
    # return lst

n = int(input("Enter the value of n: "))
k = int(input("Enter the number of multiples you want: "))
print(table_of_n(n, k))