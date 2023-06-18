class RepositorioPeliculas(object):
    __conn= None
    __manejador= None
    
    def __init__(self,conn,mGeneros):
        self.__conn= conn
        diccionario= self.__conn.consumirAPI()
        self.__manejador= self.__conn.decodificarDiccionario(diccionario,mGeneros)
        
    def getListaPeliculas(self):
        return self.__manejador.getListaPeliculas()