
l1 = [2,8,19,26]
l2 = [1,11,75]

def fusion(l1:list,l2:list) -> list:
    result:list = []
    while l1 and l2:
        if l1[0] >= l2[0]:
            result.append(l2.pop(0))
        else :
            result.append(l1.pop(0))
    if not l1:
        result+=l2
    if not l2:
        result+=l1
    return result

print(fusion(l1,l2))