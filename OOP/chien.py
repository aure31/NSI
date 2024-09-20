class chien  :
    def __init__(self,nom:str,poids:float) -> None:
        self.__poids = poids
        self.__nom = nom

    def donne_nom(self)->str:
        return self.__nom
    
    def donne_poids(self)->int:
        return self.__poids
    
    def machouille(self,jouet:str)->str:
        return jouet[:-1]
    
    def mange(self,ration:float)->bool:
        if not (ration > 0 and ration < self.__poids/10):
            return False
        self.__poids += ration
        return True

    def aboie(self,n_fois:int)->str:
        return "Ouaf "*n_fois