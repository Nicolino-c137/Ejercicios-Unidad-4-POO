from tkinter import *
from tkinter import ttk, messagebox
import math

class Aplicacion():
    __ventana= None
    __precioAñoBase= None
    __precioAñoActual= None
    __IPC= None
    __vestimenta= None
    __alimentos= None
    __educacion= None
    
    def __init__(self):
        self.__ventana= Tk()
        self.__ventana.title("Calculadora IPC")  
        self.__ventana.resizable(0,0)  
        self.__vestimenta= StringVar()
        self.__alimentos= StringVar()
        self.__educacion= StringVar()
        self.__IPC= DoubleVar()
        self.marco= ttk.Frame(self.__ventana,borderwidth=2,padding=(15,15))
        self.marco.columnconfigure(0,weight=1)
        self.marco.rowconfigure(0,weight=1)
        self.marco.grid(column=0,row=0,sticky=(N,W,E,S))
        ttk.Label(self.marco,text="Vestimenta",padding=(5,5)).grid(column=0,row=1)
        ttk.Label(self.marco,text="Alimentos",padding=(5,5)).grid(column=0,row=2)
        ttk.Label(self.marco,text="Educación",padding=(5,5)).grid(column=0,row=3)
        ttk.Label(self.marco,text="Item",padding=(5,5)).grid(column=0,row=0)
        ttk.Label(self.marco,text="Cantidad",padding=(5,5)).grid(column=1,row=0)
        ttk.Label(self.marco,text="Precio Año Base",padding=(5,5)).grid(column=2,row=0)
        ttk.Label(self.marco,text="Precio Año Actual",padding=(5,5)).grid(column=3,row=0)
        ttk.Label(self.marco,text="IPC %",padding=(5,5)).grid(column=0,row=9,rowspan=3,sticky=W)
        ttk.Label(self.marco,text='%',padding=(5,5)).grid(column=2,row=9,sticky=W)
        ttk.Label(self.marco,textvariable=self.__IPC,padding=(5,5)).grid(column=1,row=9,sticky=W)
        self.ctext1= ttk.Entry(self.marco,width=10)
        self.ctext1.grid(column=1,row=1)
        self.ctext2= ttk.Entry(self.marco,width=10)
        self.ctext2.grid(column=1,row=2)
        self.ctext3= ttk.Entry(self.marco,width=10)
        self.ctext3.grid(column=1,row=3)
        self.ctext4= ttk.Entry(self.marco,width=10)
        self.ctext4.grid(column=2,row=1)
        self.ctext5= ttk.Entry(self.marco,width=10)
        self.ctext5.grid(column=2,row=2)
        self.ctext6= ttk.Entry(self.marco,width=10)
        self.ctext6.grid(column=2,row=3)
        self.ctext7= ttk.Entry(self.marco,width=10)
        self.ctext7.grid(column=3,row=1)
        self.ctext8= ttk.Entry(self.marco,width=10)
        self.ctext8.grid(column=3,row=2)
        self.ctext9= ttk.Entry(self.marco,width=10)
        self.ctext9.grid(column=3,row=3)
        ttk.Label(self.marco,width=10).grid(column=1,row=5)
        ttk.Button(self.marco,text="Calcular IPC",padding=(1,1),command=self.calcular).grid(column=1,row=6)
        ttk.Button(self.marco,text="Salir",padding=(1,1),command=quit).grid(column=3,row=6)
    
    def calcular(self):
        try:
            sumatoriaItems= int(self.ctext1.get()+self.ctext2.get()+self.ctext3.get())
            valorCanastaAñoActual= float(float(self.ctext7.get()+self.ctext8.get()+self.ctext9.get())*sumatoriaItems)
            valorCanastaAñoBase= float(float(self.ctext4.get()+self.ctext5.get()+self.ctext6.get())*sumatoriaItems)
            ipc= valorCanastaAñoActual/valorCanastaAñoBase
            decimal= math.modf(ipc)
            porcentual= decimal[0]*100
            self.__IPC.set(porcentual)
        except ValueError:
            messagebox.showerror(title="Error",message="Debe ingresar un valor numérico") 
                
    def ejecutar(self):
        self.__ventana.mainloop()