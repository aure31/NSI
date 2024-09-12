def nombre_entier(message="Saisir un nombre entier : "):
    n = int(input(message))
    if n < 0:
        return nombre_entier("erreur n'acepte que des nombre entier : ")
    return n

#nombre_entier()

#EXERCICE 2
def adherents(n=20,ade=2000,tab=[]):
    if n == 0:
        return tab
    ade = ade*0.95+200
    tab.append(ade)
    return adherents(n-1,ade,tab)
#nombre = eval(input("Saisir le nombre d'année : "))
#print(adherents())

#EXERCICE 3
def expo(x,y):
    if y == 0:
        return x
    if y %2 == 0:
        return expo(x*x,y//2)
    return expo(x,y-1)*x

#print(expo(2,3))

#EXERCICE 4
def somme_carre(l):
    if len(l) == 0:
        return 0
    return l[0]*l[0] + somme_carre(l[1:])

def liste_des_positifs(l,tab=[]):
    if len (l) == 0:
        return tab
    if l[0] > 0:
        tab.append(l[0])
    return liste_des_positifs(l[1:],tab)

#print(liste_des_positifs([1,2,3,4,5,-1,-2,-3,-4,-5]))
#print(somme_carre([1,2,3,4,5]))

#EXERCICE 5
def multiplication(a,b,result=0):
    if b > a:
        a,b = b,a
    if b == 0:
        return result
    return multiplication(a,b-1,result+a)

def puissance(a:int,b:int,result=1):
    if b == 0:
        return result
    return puissance(a,b-1,multiplication(result,a))

#print(puissance(6,10))

#EXERCICE 6

#1 
