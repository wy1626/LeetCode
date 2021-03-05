
def approximation(number):
    tmp = number*10
    if tmp%10 < 5:
        result = int(tmp//10)
    else:
        result = int(tmp//10)+1
    return result

print(approximation(5.1))
print(approximation(5.5))
print(approximation(5.03))


# print(51.5%10)
# print(55.5%10)
# print(int(55.5//10))