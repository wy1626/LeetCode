# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


# 思路：暴力枚举
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
# def twoSum(nums,target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i]+nums[j] == target:
#                  return [i,j]

# l = [2,7,11,15]
# t = 9
# print(twoSum(l,t))


nums = [2,7,1,5]
print(enumerate(nums))
