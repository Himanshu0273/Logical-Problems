# Problem Statement:
# You are given an array of n stalls at various positions along a straight line. You also have k cows that need to be placed in these stalls such that the minimum distance between any two cows is as large as possible.
# Place the cows in the stalls to maximize the minimum distance between any two of them.

# Example:
# Input:
# stalls = [1, 2, 8, 4, 9]
# k = 3
# Output:
# 3
# Explanation:
# Cows can be placed at positions 1, 4, and 8 or 1, 4, and 9.The minimum distance between any two cows is **3**, which is the largest possible.

def canPlace(arr, k, dist):
    last=arr[0]
    c=1
    for i in range(1, len(arr)):
        if arr[i]-last>=dist:
            c+=1
            last=arr[i]
        if c==k:
            return True        
    return False

arr=[1, 2, 8, 4, 9]
arr = sorted(arr)
k=3
l=1
r=arr[len(arr)-1] - arr[0]

while l<=r:
    mid = l+(r-l)//2
    if canPlace(arr, k, mid):
        l=mid+1
    else:
        r=mid-1
        
print(r)