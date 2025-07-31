'''import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(text="Ingrese nombre de usuario:")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=30, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2=ttk.Label(text="Ingrese clave:")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.ventana1, width=30, textvariable=self.dato2, show="*")
        self.entry2.grid(column=1, row=1)
        self.boton1=ttk.Button(self.ventana1, text="Ingresar", command=self.ingresar)
        self.boton1.grid(column=1, row=2)
        self.ventana1.mainloop()

    def ingresar(self):
        if self.dato1.get()=="juan" and self.dato2.get()=="abc123":
            self.ventana1.title("Correcto")
        else:
            self.ventana1.title("Incorrecto")

aplicacion1=Aplicacion()'''

#---------ATENCIÓN!!----- la clase 'Listbox' la recuperamos del módulo tkinter 
#a través de su alias tk.Pero,Si tratamos de recuperarla del otro módulo se nos 
#informará que no existe mediante un mensaje de error:

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.listbox1=tk.Listbox(self.ventana1)
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"papa")
        self.listbox1.insert(1,"manzana")
        self.listbox1.insert(2,"pera")
        self.listbox1.insert(3,"sandia")
        self.listbox1.insert(4,"naranja")
        self.listbox1.insert(5,"melon")
        self.boton1=ttk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)
        self.label1=ttk.Label(text="Seleccionado:")
        self.label1.grid(column=0, row=2)        
        self.ventana1.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            self.label1.configure(text=self.listbox1.get(self.listbox1.curselection()[0]))

aplicacion1=Aplicacion()