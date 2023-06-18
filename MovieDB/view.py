import tkinter as tk

class FilmList(tk.Frame):
    
    def __init__(self,master,**kwargs):
        super().__init__(master)
        self.lb= tk.Listbox(self,**kwargs)
        scroll= tk.Scrollbar(self,command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT,fill=tk.Y)
        self.lb.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)
        
    def insertar(self,pelicula,index=tk.END):
        text= f"{pelicula.getTitulo()}"
        self.lb.insert(index,text)
        
    def bind_doble_click(self,callback):
        handler= lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>",handler) 

class FilmDetail(tk.Frame):
    fields= ("Título","Sinopsis","Lenguaje Original","Fecha de Lanzamiento","Géneros","Puntuación Promedio")
    
    def __init__(self,master,**kwargs):
        super().__init__(master,padx=10,pady=10,**kwargs)
        self.frame= tk.Frame(self)
        self.frame.pack()
        self.labels= list(map(self.crearCampo,enumerate(self.fields)))
        
    def crearCampo(self,field):
        position, text= field
        label1= tk.Label(self.frame,text= text)
        label2= tk.Entry(self.frame,width=25)
        label1.grid(row=position,column=0,pady=5)
        label2.grid(row=position,column=1,pady=5)
        return label2
    
    def mostrarEstadoPelicula(self,pelicula):
        values= (pelicula.getTitulo(),pelicula.getSinopsis(),pelicula.getLenguaje(),pelicula.getFechaLanzamiento(),pelicula.getGeneros(),pelicula.getPuntuacion())
        for label, value in zip(self.labels,values):
            label.delete(0,tk.END)
            label.insert(0,value)

class FilmsViews(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Movie DB")
        self.list= FilmList(self,height=15)
        self.list.pack(side=tk.LEFT,padx=10,pady=10)
        self.form= FilmDetail(self)
        self.form.pack(padx=10,pady=10)
        
    def setControlador(self,ctrl):
        self.list.bind_doble_click(ctrl.seleccionarPelicula)
    
    def agregarPelicula(self,pelicula):
        self.list.insertar(pelicula)
    
    def verPelicula(self,pelicula):
        self.form.mostrarEstadoPelicula(pelicula)