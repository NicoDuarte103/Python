import tkinter as tk

class ventana1():

    def __init__(self,root):
        self.ventana = root
        

    def datos(self):
        self.entrada = tk.Entry(self.ventana)
        self.entrada.pack()
        self.boton= tk.Button(self.entrada,text="siguiente",command=self.otraventana)
        self.ventana.mainloop()
    def otraventana(self):
        self.ventana.destroy()
        self.ventana2 = tk.Tk()
        self.ventana2_app = ventana2(self.ventana2)
        self.ventana2.mainloop()

class ventana2(ventana1):
    def __init__(self,root):
        super().__init__(root)
    def mostrar_datos():
        self.resultado = self.entrada.get()
        print(self.resultado)
    
root = tk.Tk()
ejecucion = ventana1(root)
ejecucion.datos()