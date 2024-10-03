class Pile():

    def __init__(self):
        self.__taille = 0
        self.__elements = []

    def empiler(self, element):
        self.__taille +=1
        self.__elements.append(element)

    def depiler(self):
        if self.__taille > 0:
            self.__taille -= 1
            return self.__elements.pop()

    def pile_vide(self):
        return self.__taille == 0


    def sommet(self):
        if self.__taille > 0:
            return self.__elements[-1]
    

    def __str__(self):
        return str(self.__elements)

class File:
    def __init__(self):
        self.__taille = 0
        self.__elements = []


    def file_vide(self):
        return self.__taille == 0

    def enfile(self, x):
        self.__elements.insert(0,x)
        self.__taille += 1

    def defile(self):
        if self.file_vide():
            print("File vide !!")
        else:
            self.__taille -= 1
            return self.__elements.pop()

    def __str__(self):
        return str(self.__elements)

