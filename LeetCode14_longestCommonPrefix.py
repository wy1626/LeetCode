# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 所有输入只包含小写字母 a-z 

# 思路：纵向比较
def longestCommonPrefix(strs):
    if not strs:
        return ''

    count = len(strs)
    length = len(strs[0])
    for j in range(length):
        for i in range(1,count):
            if j== len(strs[i]) or strs[i][j] != strs[0][j]:    # 注意条件顺序
                return strs[0][:j]
    return strs[0]

strs1 = []
strs2 = ['']
strs3 = ["flower","flow","flight"]
strs4 = ["dog","dog","dog"]
strs5 = ["dog","racecar","car"]
print(longestCommonPrefix(strs1))
print(longestCommonPrefix(strs2))
print(longestCommonPrefix(strs3))
print(longestCommonPrefix(strs4))
print(longestCommonPrefix(strs5))

# 横向比较
def longestCommonPrefix2(strs):

    if not strs:
        return ''

    prefix = strs[0]
    count = len(strs)
    for i in range(1,count):
        prefix = lcp(prefix,strs[i])
        if not prefix:
            return ''
    return prefix

def lcp(s1,s2):
    length = min(len(s1),len(s2))
    common = ''
    for i in range(length):
        if s1[i] == s2[i]:
            common+=s1[i]
        else:
            return common
    return common

strs1 = []
strs2 = ['']
strs3 = ["flower","flow","flight"]
strs4 = ["dog","dog","dog"]
strs5 = ["dog","racecar","car"]
print(longestCommonPrefix2(strs1))
print(longestCommonPrefix2(strs2))
print(longestCommonPrefix2(strs3))
print(longestCommonPrefix2(strs4))
print(longestCommonPrefix2(strs5))

# 分治


# 二分查找

