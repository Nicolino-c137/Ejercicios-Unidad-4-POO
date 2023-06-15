from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion:
    __ventanaPrincipal= None
    __iva= None
    __opcion= None
    __precioBase= None
    __precioConIVA= None
    
    def __init__(self):
        self.__ventanaPrincipal= Tk()
        self.__ventanaPrincipal.title("Calculadora de IVA")
        self.__ventanaPrincipal.geometry("250x260")
        self.__ventanaPrincipal.resizable(0,0)
        self.variables()
        self.frames()
        self.labels_Entrys()
        self.buttons()
        
        
    def variables(self):
        self.__iva= StringVar()
        self.__opcion= IntVar()
        self.__precioBase= StringVar()
        self.__precioConIVA= StringVar()
    
    def frames(self):
        s= ttk.Style()
        s.configure("Marco1.TFrame",background="lightblue")
        self.marco1= ttk.Frame(self.__ventanaPrincipal,borderwidth=2,padding=(5,5),style="Marco1.TFrame")
        self.marco1.grid(row=0)
        styleSeparator= ttk.Style()
        styleSeparator.configure("TSeparator",background="grey")
        separator= ttk.Separator(self.__ventanaPrincipal,orient=HORIZONTAL,style="TSeparator")
        separator.grid(row=2,padx=1,sticky=(N,W,E,S))   
        self.marco2= ttk.Frame(self.__ventanaPrincipal,borderwidth=20,padding=(5,5))
        self.marco2.grid(row=3,sticky=(N,W,E,S))
        
    def labels_Entrys(self):
        styleLabel= ttk.Style()
        styleLabel.configure("Label1.TLabel",background="lightblue")
        ttk.Label(self.marco1,text="Cálculo de IVA",padding=(5,5),style="Label1.TLabel").grid(row=0,padx=75,sticky=(N,W,E,S))
        ttk.Label(self.marco2,text="Precio sin IVA",padding=(5,5)).grid(column=0,row=4,padx=5,pady=5)
        styleEntry= ttk.Style()
        styleEntry.configure("TEntry",padding=(5,2),background="black")
        ttk.Entry(self.marco2,style="TEntry",textvariable=self.__precioBase,width=12).grid(column=1,row=4,padx=5,pady=5)
        ttk.Entry(self.marco2,style="TEntry",textvariable=self.__iva,width=12).grid(column=1,row=7,rowspan=1)
        ttk.Entry(self.marco2,style="TEntry",textvariable=self.__precioConIVA,width=12).grid(column=1,row=8,rowspan=1)
        ttk.Label(self.marco2,text="IVA",padding=(2,2)).grid(column=0,row=7,padx=5,pady=5)
        ttk.Label(self.marco2,text="Precio con IVA",padding=(2,2)).grid(column=0,row=8,padx=5,pady=5)        
        
    def buttons(self):
        ttk.Radiobutton(self.marco2,text="IVA 21%",value=21,variable=self.__opcion).grid(row=5,column=0,sticky=W)
        ttk.Radiobutton(self.marco2,text="IVA 10.5%",value=10,variable=self.__opcion).grid(row=6,column=0,sticky=W)        
        ttk.Button(self.marco2,text="Calcular",padding=(1,1),command=self.calcular).grid(column=0,row=9,pady=5)
        ttk.Button(self.marco2,style="Salir.TButton",text="Salir",padding=(1,1),command=quit).grid(column=1,row=9,pady=5)
   
    def calcular(self):
        try:
            if int(self.__opcion.get()) == 21:
                self.__precioConIVA.set(float(self.__precioBase.get())*1.21)
                self.__iva.set(21)
            elif int(self.__opcion.get()) == 10:
                self.__precioConIVA.set(float(self.__precioBase.get())*1.105)
                self.__iva.set(10.5)
        except ValueError:
            messagebox.showerror(title="Error",message="Debe ingresear un valor numérico")
        
    def ejecutar(self):
        self.__ventanaPrincipal.mainloop()