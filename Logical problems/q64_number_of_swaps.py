#Return number of swaps performed to sort a list

def count_swaps(arr):
    c=0
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                c+=1
                arr[j+1],arr[j]=arr[j],arr[j+1]
                
    print(arr)
                
    print("Number of swaps required: ", c)

arr=[5, 4, 3, 2]
count_swaps(arr)
