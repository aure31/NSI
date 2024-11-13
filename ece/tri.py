
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
    
print(chercher_rec([1,1,1,1,1,4,5,6,7,9,12,12,12,12,12],5,0,14))