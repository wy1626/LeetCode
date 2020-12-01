def twoSum(nums,target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                 return [i,j]

l = [2,7,11,15]
t = 9
print(twoSum(l,t))