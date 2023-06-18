class ManejadorGeneros:
    __generos= list
    
    def __init__(self):
        self.__generos= []
        
    def addGenero(self,genero):
        self.__generos.append(genero)
        
    def getNombresSegunId(self,id):
        nombres= []
        for i in range(len(id)):
            k=0
            bandera= False
            while not bandera and k < len(self.__generos):
                if self.__generos[k].getID() == int(id[i]):
                    bandera= True
                    nombres.append(self.__generos[k].getNombre())
                k+= 1
        return nombres