from queue import Queue

def cree_arbre(r=None):
    """renvoie un arbre vide ou un arbre de racine r"""
    if r is not None:
        return [r, [], [] ]
    else :
        return []
    

def arbre_vide(a):
    return a== []

def fils_gauche(a):
    if not arbre_vide(a):
        return a[1]
    
def insere(a,val):
    if arbre_vide(a):
        a.append(val)
        a.append([])
        a.append([])
    elif val <= a[0]:
        insere(a[1],val)
    else : insere(a[2],val)

#a = [12, 15, 14, 8, 17]
#a = [15, 12, 14, 8, 17]
#arbre = cree_arbre()
#for e in a:
#    insere(arbre,e)
#print( arbre)

class Arbre:
    def __init__(self, valeur,parent = None):
        self.valeur = valeur
        self.gauche = None
        self.droite = None
        self.parent = parent

    def __str__(self):
        return self.repr()
    
    def repr(self,i=0,tab=""):
        r,l = "",""
        if (self.droite != None) :
            r += self.droite.repr(i+1,"/-------")
            
        if (self.gauche != None) :
            l += self.gauche.repr(i+1,"\\-------")
            
        if i !=0:
            tab = "\t" * (i -1) + tab

        return r + tab + str(self.valeur) + "\n" + l
    
    def affiche_valeur(self):
        return ","+str(self.valeur)+" "
    
    def prefix(self,tab = []):
        if self.valeur:
            tab.append(self.valeur)
            if self.gauche : 
                g =self.gauche.prefix(tab)
                if not g : 
                    tab.append(g)
            if self.droite : 
                d =self.droite.prefix(tab)
                if not d : 
                    tab.append(d)
            return tab
        return None
    
    def infixe(self,tab = []):
        if self.valeur:
            if self.gauche : 
                g =self.gauche.infixe(tab)
                if not g : 
                    tab.append(g)
            tab.append(self.valeur)
            if self.droite : 
                d =self.droite.infixe(tab)
                if not d : 
                    tab.append(d)
            return tab
        return None

    def postfix(self,tab = []):
        if self.valeur:
            if self.gauche : 
                g =self.gauche.postfix(tab)
                if not g : 
                    tab.append(g)
            if self.droite : 
                d =self.droite.postfix(tab)
                if not d : 
                    tab.append(d)
            tab.append(self.valeur)
            return tab
        return None
    
    def parc_largeur(self):
        tab=[]
        f = Queue(self.taille())
        f.put(self)
        while not f.empty() :
            a = f.get()
            tab.append(a.valeur)
            if a.gauche is not None :
                f.put(a.gauche)
            if a.droite : 
                f.put(a.droite)
        return tab

    def ajoute(self, valeur):
        if valeur <= self.valeur:
            if self.gauche is None:
                self.gauche = Arbre(valeur,self)
            else:
                self.gauche.ajoute(valeur)
        elif valeur > self.valeur:
            if self.droite is None:
                self.droite = Arbre(valeur,self)
            else:
                self.droite.ajoute(valeur)

    def enfant_gauche(self):
        return self == self.parent.gauche
    
    def enfant_gauche(self):
        return self == self.parent.droite

    def taille(self):
        t=0
        if self.gauche:
            t+=self.gauche.taille()
        if self.droite:
            t+=self.droite.taille()
        return t+1

    def affiche(self, niveau=0):
        if self.droite :
            self.droite.affiche(niveau + 1)
        print(niveau * "\t", self.valeur)
        if self.gauche :
            self.gauche.affiche(niveau + 1)

    #Exercice 1
    # 1)
    def recherche(self,val):
        a,b = None,None
        if val == self.valeur:
            return True
        if self.droite:
            a = self.droite.recherche(val)
        if self.gauche:
            b = self.gauche.recherche(val)
        if a is None and b is None and val != self.valeur:
            return False
        return max(a,b)
    
    #2 )
    def minimum(self):
        if self.droite: return self.droite.minimum()
        else : return self.valeur

    def maximum(self):
        if self.droite : return self.droite.maximum()
        else : return self.valeur

    def successeur(self,prec = None):
        if prec == None :
            prec = self.valeur
            if self.droite: 
                return self.droite.successeur(prec)
        elif self.gauche and prec < self.valeur :
            return self.gauche.successeur(prec)
        elif self.droite and prec >= self.valeur:
            return self.droite.successeur(prec)
        else:
            return self.valeur
        
    def predecesseur(self,prec = None):
        if prec == None :
            prec = self.valeur
            if self.gauche: 
                return self.gauche.successeur(prec)
        elif self.droite and prec < self.valeur :
            return self.droite.successeur(prec)
        elif self.gauche and prec >= self.valeur:
            return self.gauche.successeur(prec)
        else:
            return self.valeur


a = [17, 25, 11, 13, 23, 5, 8 , 28,9]
arbre = Arbre(a.pop(0))
for e in a :
    arbre.ajoute(e)
print(arbre)

#Exercice 3 :
'''
1)
prefix : H,R,I,A,K,J,M,S,L,O
infix : I,R,K,A,H,J,S,M,L,O
postfix : I,K,A,R,S,O,L,M,J,H

2)


'''
#Exercice 4 : 
'''
1)
oui il est possible car chaque valeur suit le principe d'un arbre binaire de recherche

2)
non car 22 serais mit à droite de 23 donc ce chemin n'est pas valide
'''

#Exercice 5 :






