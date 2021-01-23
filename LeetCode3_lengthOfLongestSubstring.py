# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 暴力破解
def lengthOfLongestSubstring(s):
    
    count = len(s)

    if count == 0:
        return 0
    
    length = 0
    for i in range(count):
        common = s[i]
        for j in range(i+1,count):
            if s[j] not in common:
                common += s[j]
            else:
                break
        length = max(length,len(common))
    
    return length

s1 = 'abcabcbb'
s2 = 'bbbbb'
s3 = 'pwwkew'
s4 = ''

print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))
print(lengthOfLongestSubstring(s4))