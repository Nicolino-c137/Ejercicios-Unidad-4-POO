from fractions import Fraction

class Imaginario:
    __real= int
    __imaginario= int
    
    def __init__(self,real,imaginario=None):
        self.__real= real
        if imaginario == None:
            self.__imaginario= -1
        else:
            self.__imaginario= imaginario
    
    def __add__(self,otro):
        sumaReal= self.__real + otro.__real
        sumaImaginaria= self.__imaginario + otro.__imaginario
        return Imaginario(sumaReal,sumaImaginaria)
    
    def __sub__(self,otro):
        restaReal= self.__real - otro.__real
        restaImaginaria= self.__imaginario - otro.__imaginario
        return Imaginario(restaReal,restaImaginaria)
    
    def __mul__(self,otro):
        mulReal= (self.__real * otro.__real) - (self.__imaginario * otro.__imaginario)
        mulImaginaria= (self.__real * otro.__imaginario) + (self.__imaginario * otro.__real)
        return Imaginario(mulReal,mulImaginaria)
    
    def __truediv__(self,otro):
        denominador= (otro.__real ** 2) + (otro.__imaginario ** 2)
        divisionReal= Fraction(str((((self.__real * otro.__real) + (self.__imaginario * otro.__imaginario))/denominador))).limit_denominator()
        divisionImaginaria= Fraction(str((((self.__imaginario * otro.__real) - (self.__real * otro.__imaginario))/denominador))).limit_denominator()
        return Imaginario(divisionReal,divisionImaginaria)
    
    def __str__(self):
        if self.__imaginario < 0:
            resultado= f"{self.__real}{self.__imaginario}i"
        else:
            resultado= f"{self.__real}+{self.__imaginario}i"
        return resultado