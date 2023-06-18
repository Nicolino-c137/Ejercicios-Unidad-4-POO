class Pelicula(object):
    __titulo= str
    __sinopsis= str
    __lenguajeOriginal= str
    __fechaLanzamiento= str
    __generos= list
    __puntuacionPromedio= float
    
    def __init__(self,titulo,sinopsis,lenguaje,fecha,generos,puntuacion):
        self.__titulo= titulo
        self.__sinopsis= sinopsis
        self.__lenguajeOriginal= lenguaje
        self.__fechaLanzamiento= fecha
        self.__generos= generos
        self.__puntuacionPromedio= puntuacion
        
    def getTitulo(self):
        return self.__titulo
        
    def getSinopsis(self):
        return self.__sinopsis
    
    def getLenguaje(self):
        return self.__lenguajeOriginal
    
    def getFechaLanzamiento(self):
        return self.__fechaLanzamiento
    
    def getGeneros(self):
        return self.__generos
            
    def getPuntuacion(self):
        return self.__puntuacionPromedio