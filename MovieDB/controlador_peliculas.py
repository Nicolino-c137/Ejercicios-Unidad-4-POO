from view import FilmsViews
from Model.manejador_peliculas import ManejadorPeliculas

class ControladorPeliculas(object):
    
    def __init__(self,repo,vista):
        self.repo= repo
        self.vista= vista
        self.seleccion= -1
        self.peliculas= list(repo.getListaPeliculas())
        
    def seleccionarPelicula(self,index):
        self.seleccion= index
        pelicula= self.peliculas[index]
        self.vista.verPelicula(pelicula)
        
    def start(self):
        for p in self.peliculas:
            self.vista.agregarPelicula(p)
        self.vista.mainloop()