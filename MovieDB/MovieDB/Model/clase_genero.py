class Genero:
    __id= int
    __nombre= str
    
    def __init__(self,id,nombre):
        self.__id= id
        self.__nombre= nombre
        
    def getID(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre