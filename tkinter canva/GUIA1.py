import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=0)
        self.canvas1.create_line(550, 370, 370,350, fill="turquoise2")
        self.canvas1.create_rectangle(10,10, 100,100, fill="pink")
        self.canvas1.create_rectangle(50,150, 250,250, fill="white")
        self.canvas1.create_oval(300,10,400,150, fill="yellow")
        self.canvas1.create_arc(420,10,550,110, fill="blue", start=180, extent=90)
        self.canvas1.create_oval(300,210,400,350, outline="green")
        self.canvas1.create_rectangle(150,15,250,115, fill="red",outline="blue1")    
        self.canvas1.create_polygon(150, 400, 0, 300,300,300, fill="magenta3")
        self.ventana1.mainloop()
aplicacion1=Aplicacion()