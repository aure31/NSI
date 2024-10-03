import Data_Struct as d


#Exercice 4
p1 = d.Pile()
f1 = d.File()
for e in range(10):
    p1.empiler(e)
    f1.enfile(e)

def pair(pile:d.Pile):
    p2 = d.Pile()
    p3 = d.Pile()
    while not pile.pile_vide():
        e = pile.depiler()
        if e %2 == 0:
            p3.empiler(e)
        else:
            p2.empiler(e)
    while not p3.pile_vide():
        p2.empiler(p3.depiler())
    return p2

def copie_pair(pile:d.Pile):
    p2 = d.Pile()
    p3 = d.Pile()
    while not pile.pile_vide():
        e = pile.depiler()
        p2.empiler(e)
        if e%2 == 0:
            p3.empiler(e)
    while not p2.pile_vide():
        pile.empiler(p2.depiler())
    while not p3.pile_vide():
        p2.empiler(p3.depiler())
    return p2

print(copie_pair(p1),p1)

#Exercice 5
def decToBin(n:int):
    pile = d.Pile()
    while n != 0:
        pile.empiler(n%2)
        n //= 2
    return pile

#Exercice 6
def inverser(file:d.File):
    f2 = d.File()
    pile = d.Pile()
    p2 = d.Pile()
    while not file.file_vide():
        pile.empiler(file.defile())
    while not pile.pile_vide():
        p2.empiler(pile.depiler())
    while not p2.pile_vide():
        f2.enfile(p2.depiler())
    return f2

#print(inverser(f1))

#Exercice 8






    