#Remove 25% from all numbers other than the smallest

def show_the_love(nums):
    mini = min(nums)
    c=0
    for i in range(len(nums)):
        if nums[i]!=mini:
            s = nums[i]*0.25
            nums[i] -= s
            c+=s
    ind = nums.index(mini)
    nums[ind]+=c
    return nums            
            
nums = [16, 10, 8]
print(show_the_love(nums))