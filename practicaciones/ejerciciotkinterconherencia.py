import tkinter as Tk

class Base():

    def __init__(self,root):
        self.ventana = root
        
    def crear_boton(self,texto,comando):
        self.boton = Tk.Button(self.ventana,text=texto,command=comando)
        self.boton.pack()


class ventana1(Base):

    def __init__(self,root):
        super().__init__(root)
        self.crear_boton ("ventana2",self.cambiar_ventana)

    def cambiar_ventana(self):
        self.ventana.destroy()
        self.ventana2=Tk.Tk()
        self.ventana2_app= ventana2(self.ventana2)
        self.ventana2.mainloop()

class ventana2(Base):
    def __init__(self,root):
        super().__init__(root)
        self.crear_boton ("ventana1",self.cambiar_ventana)

    def cambiar_ventana(self):
        self.ventana.destroy()
        self.ventana=Tk.Tk()
        self.ventana1_app= ventana1(self.ventana)
        self.ventana.mainloop()
root = Tk.Tk()
ventana1_app = ventana1(root)
root.mainloop()
