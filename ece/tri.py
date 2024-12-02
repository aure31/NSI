
# 22-38 ex 1
def tri_selection(tab:list) -> list:
    '''
    permet de trier une list par ordre croissant
    entré : une list
    sortie : ranvoie la list trier
    '''
    for i in range(len(tab)):
        imin = i 
        for j in range(i+1,len(tab)):
            if tab[imin] > tab[j]:
                imin = j
        tab[i],tab[imin] = tab[imin],tab[i]
    return tab

#print(tri_selection([1,52,6,-9,12]))

# ex 22-1 ex 1
def recherche(caractere:str,mot:str):
    count = 0
    for e in mot:
        if e == caractere:
            count+=1
    return count

#print(recherche('e', "sciences"))

#EX 22-19 ex 2
def chercher_rec(T:list,n:int,i:int,j:int) :
    if i < 0 or j > len(T) :
        print("Erreur")
        return None
    if i > j :
        return None
    m = (i+j) // 2
    if m != 0:
        print(m,i,j)
    if T[m] < n :
        return chercher_rec(T, n, m+1 , j)
    elif T[m] > n :
        return chercher_rec(T, n, i , m-1 )
    else :
        return m
    
#print(chercher_rec([1,1,1,1,1,4,5,6,7,9,12,12,12,12,12],5,0,14))

#EX 07 ex 1 conv binnair

def conv_bin(n):
    b=[]
    while n != 0:
        b.append(n%2)
        n //= 2
    b.reverse()
    return (b,len(b))


#EX 33 ex 1 conv binnaire

def convertir(T):
    """
    T est un tableau d'entiers, dont les éléments sont 0 ou 1 et
    représentant un entier écrit en binaire. Renvoie l'écriture
    décimale de l'entier positif dont la représentation binaire
    est donnée par le tableau T
    """
    result =0
    multy = len(T)-1
    for i in range (len(T)) :
        result += T[i] * 2**multy 
        multy -= 1
    return result


def tri_insertion(L):
    n = len(L)

    # cas du tableau vide
    if n == 0:
        return L

    for j in range(1,n):
        e = L[j]
        i = j

        # A l'etape j, le sous-tableau L[0,j-1] est trie
        # et on insere L[j] dans ce sous-tableau en determinant
        # le plus petit i tel que 0 <= i <= j et L[i-1] > L[j].
        while  i > 0 and L[i-1] > e:
            i = i-1
        
        # si i != j, on decale le sous tableau L[i,j-1] d'un cran
        # vers la droite et on place L[j] en position i
        if i != j:
            for k in range(j,i,-1):
                L[k] = L[k-1]
            L[i] = e
    return L


def occurence_lettres(phrase):
    dict = {}
    for char in phrase:
        if char in dict.keys() :
            dict[char] += 1
        else : dict[char] =1
    return dict


def fusion(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2 :
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 = i1 + 1
        else:
            L12[i] = L2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        L12[i] = L1[i1]
        i1 = i1 + 1
        i = i + 1
    while i2 < n2:
        L12[i] = L2[i2]
        i2 = i2 + 1
        i = i + 1
    return L12


print(occurence_lettres('Hello world !'))