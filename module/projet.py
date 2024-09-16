def nb_sommes(n):
    result = n
    if n == 0:
        n+=1
    for i in range(1,n):
        result += i*(n-i)

def fib(n):
    return fib_2(n)[1]

def supprime_premier(chaine, cible, result = ""):
    if len(chaine) == 0:
        return (False,result)
    elif chaine[0] == cible:
        return (True,result + chaine[1:])
    return supprime_premier(chaine[1:], cible, result + chaine[0])

def anagrammes(chaine1, chaine2):
    if len(chaine1) != len(chaine2):
        return False
    if len(chaine1) == 0:
        return True
    if chaine1[0] in chaine2:
        return anagrammes(chaine1[1:], supprime_premier(chaine2, chaine1[0])[1])
    return False

def fib_2(n):
    if n == 0:
        return (1,0)
    if n == 1:
        return (0,1)
    if n%2 == 0 :
        fn,fn2 = fib_2(n//2)
        return (fn*fn+fn2*fn2,2*fn*fn2+fn2*fn2)
    else:
        fn,fn2 = fib_2(n-1)
        return (fn2,fn+fn2)
