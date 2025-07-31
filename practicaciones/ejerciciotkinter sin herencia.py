import tkinter as tk

class ventana1():

    def __init__(self,root):

        self.ventana = root
        self.boton = tk.Button(self.ventana,text="ventana2",command=self.otraventana)
        self.boton.pack()
        self.ventana.mainloop()
    def otraventana(self):
        self.ventana.destroy()
        self.ventana_app = tk.Tk()
        self.ventana2 = ventana2(self.ventana_app)


class ventana2():

    def __init__(self,root):
        
        self.ventana2 = root
        self.boton = tk.Button(self.ventana2,text="ventana1",command=self.otraventana)
        self.boton.pack()
        self.ventana2.mainloop()
    def otraventana(self):
        self.ventana2.destroy()
        self.ventana_app = tk.Tk()
        self.ventana = ventana1(self.ventana_app)



root = tk.Tk()
ejecucion = ventana1(root)
