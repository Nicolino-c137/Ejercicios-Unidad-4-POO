class ManejadorPeliculas:
    __peliculas= list
    
    def __init__(self):
        self.__peliculas= []
        
    def addPelicula(self,pelicula):
        self.__peliculas.append(pelicula)
        
    def getListaPeliculas(self):
        return self.__peliculas   