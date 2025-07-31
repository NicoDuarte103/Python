import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.valor=1
        self.ventana1=tk.Tk()
        self.ventana1.title("Controles Button y Label")
        self.label1=tk.Label(self.ventana1, text=self.valor)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="red")#primer plano rojo

        self.boton1=tk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1)

        self.boton2=tk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)

        self.ventana1.mainloop()


    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)

    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)        


aplicacion1=Aplicacion()

#Para no permitir redimensionar ni el ancho ni el alto del la ventana debemos llamar 
#al 'método resizable' y pasar el valor False a cada parámetro.
'''import tkinter as tk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Prueba")
        self.label1=tk.Label(self.ventana1, text="Sistema de facturación")
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(self.ventana1, text="2018")
        self.label2.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Finalizar", command=self.finalizar)
        self.boton1.grid(column=0, row=2)
        self.ventana1.resizable(False, False)
        self.ventana1.mainloop()


    def finalizar(self):
        sys.exit(0)# finalizar un programa en Python debemos llamar a la función exit que se encuentra en el módulo sys,
                   # por ello hemos importado dicho módulo al principio

aplicacion1=Aplicacion()'''