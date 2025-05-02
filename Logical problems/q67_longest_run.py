#What is the longest consecutive run in the giving array?(Increasing or Decreasing)

def longest_run(arr):
    maxi = 0
    maxd = 0
    ic=1
    dc=1
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1])==1:
            if arr[i]<arr[i+1]:
                ic+=1
                maxd = max(maxd, dc)
                dc=1    
            
            else:
                dc+=1
                maxi=max(maxi, ic)
                ic=1
        else:
            ic=1
            dc=1
            
    maxi=max(maxi,ic)
    maxd=max(maxd,dc)

    print("Longest Consecutive sequence is: ", max(maxi, maxd))
    
    
def func2(arr):
    maxi=0
    ic=1
    dc=1
    
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]-1:
            ic+=1
            dc=1
        elif arr[i]==arr[i+1]+1:
            dc+=1
            ic=1
            
        else:
            ic=dc=1
        maxi=max(maxi, max(ic, dc))
        
    print("Longest Consecutive sequence is: ", maxi)
    
nums = [1, 2, 3, 5, 6, 7, 8, 9]
# longest_run(nums)
func2(nums)