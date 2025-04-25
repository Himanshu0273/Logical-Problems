def merge(arr):
    if len(arr)>1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        
        merge(left)
        merge(right)
        
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k] = left[i]
                i+=1
                
            else:
                arr[k] = right[j]
                j+=1
                
            k+=1
            
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
            
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        
        
arr = [7,3,4,6,2,5,9]
merge(arr)
print(arr)