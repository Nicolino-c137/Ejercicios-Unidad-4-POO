from Model.objectEncoder import ObjectEncoder
from Model.repositorio_peliculas import RepositorioPeliculas
from view import FilmsViews
from controlador_peliculas import ControladorPeliculas

if __name__ == "__main__":
   conn= ObjectEncoder("generos.json")
   diccionario= conn.leerJSONArchivo()
   manejadorGeneros= conn.decodificarIDGeneros(diccionario)
   repositorio= RepositorioPeliculas(conn,manejadorGeneros)
   vista= FilmsViews()
   ctrl= ControladorPeliculas(repositorio,vista)
   vista.setControlador(ctrl)
   ctrl.start()