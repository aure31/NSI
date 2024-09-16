def somme(l:list)->float:
    a = 0
    for i in l:
        a += i
    return a

def moyenne(l:list)->float:
    a = somme(l)
    return a/len(l)