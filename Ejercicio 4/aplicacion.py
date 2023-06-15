import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
from clase_imaginario import Imaginario

class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primerOperando=None
    __segundoOperando=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        self.mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe['borderwidth'] = 2
        self.mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None
        operatorEntry=ttk.Entry(self.mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        self.panelEntry = ttk.Entry(self.mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled')
        self.panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        self.estandar()
        
    def estandar(self):
        tipoN= "reales"
        ttk.Button(self.mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(self.mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(self.mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(self.mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(self.mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(self.mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(self.mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W)
        ttk.Button(self.mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(self.mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(self.mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(self.mainframe, text='+', command=partial(self.ponerOPERADOR, '+',tipoN)).grid(column=2, row=6, sticky=W)
        ttk.Button(self.mainframe, text='-', command=partial(self.ponerOPERADOR, '-',tipoN)).grid(column=3, row=6, sticky=W)
        ttk.Button(self.mainframe, text='*', command=partial(self.ponerOPERADOR, '*',tipoN)).grid(column=1, row=7, sticky=W)
        ttk.Button(self.mainframe, text='/', command=partial(self.ponerOPERADOR, '/',tipoN)).grid(column=2, row=7, sticky=W)
        ttk.Button(self.mainframe, text='=', command=partial(self.ponerOPERADOR, '=',tipoN)).grid(column=3, row=7, sticky=W)
        #Al presionar el botón imaginarios, la calculadora podrá realizar operaciones con N° imaginarios
        ttk.Button(self.mainframe, text="imaginarios", command=partial(self.cambiarTipoNumeros,"imaginarios")).grid(column=2,row=2,sticky=W)
        ttk.Button(self.mainframe, text='C', command=partial(self.borrarPanel)).grid(column=3, row=2, sticky=W)
        self.__panel.set('0')
        self.panelEntry.focus()
        
    def imaginarios(self):
        tipoN= "imaginarios"
        #z= Imaginario()
        #w= Imaginario()    
        num1= ttk.Button(self.mainframe, text='1', command=partial(self.ponerNUMERO, '1'))
        num1.grid(column=1, row=3, sticky=W)
        num1.bind("<Button-1>",self.borrarPanel)
        ttk.Button(self.mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(self.mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(self.mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(self.mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(self.mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(self.mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W)
        ttk.Button(self.mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(self.mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(self.mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(self.mainframe, text='+', command=partial(self.ponerOPERADOR, '+',tipoN)).grid(column=2, row=6, sticky=W)
        ttk.Button(self.mainframe, text='-', command=partial(self.ponerOPERADOR, '-',tipoN)).grid(column=3, row=6, sticky=W)
        ttk.Button(self.mainframe, text='*', command=partial(self.ponerOPERADOR, '*',tipoN)).grid(column=1, row=7, sticky=W)
        ttk.Button(self.mainframe, text='/', command=partial(self.ponerOPERADOR, '/',tipoN)).grid(column=2, row=7, sticky=W)
        ttk.Button(self.mainframe, text='=', command=partial(self.ponerOPERADOR, '=',tipoN)).grid(column=3, row=7, sticky=W)
        #Al presionar el botón estandar, la calculadora podrá realizar operaciones con N° reales
        ttk.Button(self.mainframe, text="estandar", command=partial(self.cambiarTipoNumeros,"estandar")).grid(column=2,row=2,sticky=W)
        ttk.Button(self.mainframe, text='C', command=partial(self.borrarPanel)).grid(column=3, row=2, sticky=W)
        self.positivo= ttk.Button(self.mainframe, text="positivo",command=partial(self.ponerNUMERO,'+'))
        self.positivo.grid(column=4,row=2,sticky=W)
        self.negativo= ttk.Button(self.mainframe, text="negativo",command=partial(self.ponerNUMERO,'-'))
        self.negativo.grid(column=4,row=3,sticky=W)
        self.__panel.set('0')
        self.panelEntry.focus()
        
    def cambiarTipoNumeros(self,tipoN):
        if tipoN == "estandar":
            self.positivo.destroy()
            self.negativo.destroy()
            self.estandar()
        else:
            self.imaginarios()
    
    def ponerNUMERO(self, numero,tipoN):
        if tipoN == "estandar":
            if self.__operadorAux==None:
                valor = self.__panel.get()
                self.__panel.set(valor+numero)
            else:
                self.__operadorAux=None
                valor=self.__panel.get()
                self.__primerOperando=int(valor)
                self.__panel.set(numero)
        else:
            pass
            
    def borrarPanel(self):
        self.__panel.set('')
        
    def resolverOperacion(self, operando1, operacion, operando2,tipoN):
        resultado=0
        if operacion=='+':
            resultado=operando1+operando2
        else:
            if operacion=='-':
                resultado=operando1-operando2
            else:
                if operacion=='*':
                    resultado=operando1*operando2
                else:
                    if operacion=='/':
                        resultado=operando1/operando2
        self.__panel.set(str(resultado))
        
    def ponerOPERADOR(self, op,tipoN):
        if op=='=':
            operacion=self.__operador.get()
            self.__segundoOperando=int(self.__panel.get())
            self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux=None
        else:
            if self.__operador.get()=='':
                self.__operador.set(op)
                self.__operadorAux=op
            else:
                
                operacion=self.__operador.get()
                self.__segundoOperando=int(self.__panel.get())
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux=op
    
    def ejecutar(self):
        self.__ventana.mainloop()



