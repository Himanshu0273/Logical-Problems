def quick_sort(arr, left, right):
    def partition(low, high):
        pivot = arr[high]
        i=low-1
        for j in range(low, high):
            if arr[j]<=pivot:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
                
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1
    
    def qs_recursion(low, high):
        if low<high:
            pivot = partition(low, high)
            qs_recursion(low, pivot-1)
            qs_recursion(pivot+1, high)
    

    qs_recursion(0, len(arr)-1)
    return arr
arr = [4,3,5,7,3,8,4,9,1]
arr = quick_sort(arr, 0, len(arr)-1)
print(arr)

