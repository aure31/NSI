
class Complex :
    def __init__(self,reel,im) -> None:
        self.__reel = reel
        self.__im = im

    def donne_reel(self)->float:
        return self.__reel
    
    def donne_im(self)->float:
        return self.__im
    
    def __add__(self,other:Complex)->Complex:
        if(isinstance( other, Complex)):
            self.__reel+=other.donne_reel()
            self.__im+=other.donne_im()
        else:
            self.__reel+=other
        return self
    
    def __sub__(self,other:Complex)->Complex:
        if(isinstance( other, Complex)):
            self.__reel-=other.donne_reel()
            self.__im-=other.donne_im()
        else:
            self.__reel-=other
        return self
    
    def __mul__(self,other:Complex)->Complex:
        if(isinstance( other, Complex)):
            self.__reel=self.__reel*other.donne_reel()-self.__im*other.donne_im()
            self.__im=self.__reel*other.donne_im()+self.__im*other.donne_reel()
        else:
            self.__reel*=other
            self.__im*=other
        return self
    
    def conjugate(self)->Complex:
        return Complex(self.__reel,-self.__im)
    
    def is_real(self)->bool:
        return self.__im==0
    
    def is_imaginary(self)->bool:
        return self.__reel==0
    
    def is_zero(self)->bool:
        return self.__reel==0 and self.__im==0
    
    def __eq__(self, value: Complex) -> bool:
        return self.__reel==value.donne_reel() and self.__im==value.donne_im()
    
    def inverse(self) -> Complex:
        if self.is_zero():
            return None
        return Fraction(self.conjugate(),self.__reel*self.__reel+self.__im*self.__im)
    

class Fraction :

    def __init__(self,num:int,den:int) -> None:
        if den==0:
            raise ValueError("Denominator cannot be zero")
        self.__num = num
        self.__den = den

    def donne_num(self)->int:
        return self.__num
    
    def donne_den(self)->int:
        return self.__den
    
    def __add__(self,other:Fraction)->Fraction:
        self.__num = self.__num*other.donne_den() + other.donne_num()*self.__den
        self.__den = self.__den*other.donne_den()
        return self
    
    def __sub__(self,other:Fraction)->Fraction:
        self.__num = self.__num*other.donne_den() - other.donne_num()*self.__den
        self.__den = self.__den*other.donne_den()
        return self
    
    def __mul__(self,other:Fraction)->Fraction:
        self.__num = self.__num*other.donne_num()
        self.__den = self.__den*other.donne_den()
        return self
    
    def __truediv__(self,other:Fraction)->Fraction:
        self.__num = self.__num*other.donne_den()
        self.__den = self.__den*other.donne_num()
        return self
    
    def __eq__(self, value: Fraction) -> bool:
        return self.__num==value.donne_num() and self.__den==value.donne_den()
    
    def inverse(self) -> Fraction:
        if self.__num==0:
            return None
        return Fraction(self.__den,self.__num)
    
    def simplifie(self) -> Fraction:
        if self.__num==0:
            return Fraction(0,1)
        if self.__den==0:
            return None
        return Fraction(self.__num//self.__den,self.__den//self.__den)

    
