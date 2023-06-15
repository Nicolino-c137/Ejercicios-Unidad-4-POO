from tkinter import *
from tkinter import ttk,messagebox
import requests

class Aplicacion:
    __ventanaPrincipal= None
    __dolares= None
    __pesos= None
    
    def __init__(self):
        self.__ventanaPrincipal= Tk()
        self.__ventanaPrincipal.title("Conversor de moneda")
        self.__ventanaPrincipal.geometry("290x115")
        self.variables()
        self.frames()
        self.labels_Entrys()
        self.buttons()
    
    def variables(self):
        self.__dolares= StringVar()
        self.__pesos= StringVar()
        self.__dolares.trace('w',self.calcular)
    
    def frames(self):
        self.marco1= ttk.Frame(self.__ventanaPrincipal,padding="5 5 12 5",borderwidth=2,relief="sunken")
        self.marco1.grid(column=0,row=0,sticky=(N,W,E,S))
        self.marco1.columnconfigure(0,weight=1)
        self.marco1.rowconfigure(0,weight=1)
        
    def labels_Entrys(self):
        ttk.Label(self.marco1,textvariable=self.__pesos).grid(column=2,row=2,sticky=(W,E))
        ttk.Label(self.marco1,text="dólares").grid(column=3,row=1,sticky=W)
        ttk.Label(self.marco1,text="es equivalente a ").grid(column=1,row=2,sticky=E)
        ttk.Label(self.marco1,text="pesos").grid(column=3,row=2,sticky=W)
        self.entry=ttk.Entry(self.marco1,width=7,textvariable=self.__dolares)
        self.entry.grid(column=2,row=1,sticky=(W,E))
        self.entry.focus()
        
    def buttons(self):
        ttk.Button(self.marco1,text="Salir",command=self.__ventanaPrincipal.destroy).grid(column=3,row=3,sticky=W)
        for child in self.marco1.winfo_children():
            child.grid_configure(padx=5,pady=5)
            
    def consumirAPI(self):
        res= requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
        json= res.json()
        precioDolar= float(json[0]["casa"]["venta"].replace(',','.'))
        return precioDolar
        
    def calcular(self,*args):
        if self.entry.get() != '':
            try:
                precioDolarOficial= self.consumirAPI()
                valor= float(self.entry.get())*precioDolarOficial
                self.__pesos.set(valor)
            except ValueError:
                messagebox.showerror(title="Error de tipo",message="Debe ingresar un valor numérico")
                self.__dolares.set('')
                self.entry.focus()
        else:
            self.__pesos.set('')
    
    def ejecutar(self):
        self.__ventanaPrincipal.mainloop()