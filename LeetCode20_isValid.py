# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
#     左括号必须用相同类型的右括号闭合。
#     左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串

def isValid(s):
    if len(s)%2 != 0:
        return False
    
    left = []
    pairs = {
        '}':'{',
        ']':'[',
        ')':'('
    }
    for i in s:
        if i in pairs.keys():
            if not left or left[-1] != pairs[i]:
                return False
            left.pop()
        else:
            left.append(i)
    return not left

s1 = ''
s2 = '([](){})'
s3 = '({)}'
s4 = '([]'

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))
print(isValid(s4))