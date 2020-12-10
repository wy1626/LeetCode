def mergeTwoLists(l1, l2):
    length1 = len(l1)
    length2 = len(l2)

    if length1 == 0:
        return l2
    elif length2 == 0:
        return l1

    i = j = 0
    l = []
    while i < length1 and j <length2:
        if l1[i] >= l2[j]:
            l.append(l2[j])
            j+=1
        else:
            l.append(l1[i])
            i+=1
    if i == length1:
        l+=l2[j:length2]
    elif j == length2:
        l+=l1[i:length1]
    return l



l1 = []
l2 = []

# l1 = []
# l2 = [1,3,4]

# l1 = [1,2,4]
# l2 = []

# l1 = [1,2,4]
# l2 = [1,3,4]

# l1 = [1,2,4]
# l2 = [1,2,3,4,5,7]

# l2 = [1,3,5,7,9]
# l1 = [2,4,6]

print(mergeTwoLists(l1, l2))