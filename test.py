def fibonacci(n):
    if n ==0 or n == 1:
        return n
    prec = 1
    current = 1
    for i in range(n-2):
        temp,prec = prec,current
        current += temp
    print
    return current

def Max(l):
    max = 0
    for i in range(1,len(l)):
        if l[i] < 0:
            continue
        if l[i] > l[max]:
            max = i
    return max

def remove3(l,i):
    l[i]=-1
    if i+1 < len(l):
        l[i+1] = -2
    if i-1 >= 0:
        l[i-1] = -2
    return l



def max_manger(feuilles):
    for i in range(2,len(feuilles)):
        feuilles[i] = max(feuilles[i-1],feuilles[i-2]+feuilles[i])
    return feuilles[-1]

# tests

feuilles = [4, 25, 20, 8, 17]
assert max_manger(feuilles) == 42


feuilles = [4, 6, 5, 7, 4]
assert max_manger(feuilles) == 13
