# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


# 思路：暴力枚举
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
def twoSum(nums,target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                 return [i,j]
    return []

nums1 = [11,2,7,15]
nums2 = [11,1,7,15]
target = 9
print(twoSum(nums1,target))
print(twoSum(nums2,target))

# 思路：哈希表
def twoSum2( nums, target):
    tmp = {}
    for i,m in enumerate(nums):
        if target-m in tmp:
            return [tmp[target-m],i]
        else:
            tmp[m] = i
    return []

nums1 = [11,15,2,7]
nums2 = [11,15,1,7]
target = 9
print(twoSum2(nums1,target))
print(twoSum2(nums2,target))