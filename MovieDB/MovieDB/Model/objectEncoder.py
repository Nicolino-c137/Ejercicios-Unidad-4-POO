from pathlib import Path
from Model.manejador_peliculas import ManejadorPeliculas
from Model.manejador_generos import ManejadorGeneros
from Model.clase_genero import Genero
from Model.clase_pelicula import Pelicula
import json, requests

class ObjectEncoder(object):
    __pathArchivo= None    
    
    def __init__(self,archivo):
        self.__pathArchivo= archivo
    
    def consumirAPI(self):
        url= "https://api.themoviedb.org/3/discover/movie?api_key=c5534f3d06fe2a82a0409cda580a3f19"
        data= requests.get(url)
        if data.status_code == 200:
            data= data.json()
        else: print(f"Error {data.status_code}")
        return data
    
    def decodificarDiccionario(self,d,manejadorGeneros):
        manejador= ManejadorPeliculas()
        for e in d["results"]:
            titulo= e["original_title"]
            sinopsis= e["overview"]
            lenguaje= e["original_language"]
            fechaLanzamiento= e["release_date"]
            idGeneros= e["genre_ids"]
            nombres= manejadorGeneros.getNombresSegunId(idGeneros)
            generos= nombres
            puntuacion= e["vote_average"]
            una_peli= Pelicula(titulo,sinopsis,lenguaje,fechaLanzamiento,generos,puntuacion)
            manejador.addPelicula(una_peli)
        return manejador
    
    def decodificarIDGeneros(self,d):
        manejador= ManejadorGeneros()
        for e in d["genres"]:
            id= e["id"]
            nombre= e["name"]
            un_genero= Genero(id,nombre)
            manejador.addGenero(un_genero)
        return manejador
    
    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding="UTF-8") as fuente:
            diccionario= json.load(fuente)
        return diccionario