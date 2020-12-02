# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 所有输入只包含小写字母 a-z 

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

# strs = []
# strs = ['']
strs = ["flower","flow","flight"]
# strs = ["dog","dog","dog"]
# strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))

