import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.entradadatos()
        self.canvas1=tk.Canvas(self.ventana1, width=600, height=400, background="ivory3")
        self.canvas1.grid(column=0, row=1)
        self.ventana1.mainloop()

    def entradadatos(self):
        self.lf1=ttk.LabelFrame(self.ventana1,text="Cantidad de asistentes")
        self.lf1.grid(column=0, row=0, sticky="w")
        self.label1=ttk.Label(self.lf1, text="Docentes:")
        self.label1.grid(column=0,row=0, padx=5, pady=5)
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.lf1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.lf1, text="Alumnas:")
        self.label2.grid(column=0,row=1, padx=5, pady=5)
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.lf1, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)
        self.label3=ttk.Label(self.lf1, text="Alumnos:")
        self.label3.grid(column=0,row=2, padx=5, pady=5)
        self.dato3=tk.StringVar()
        self.entry3=ttk.Entry(self.lf1, textvariable=self.dato3)
        self.entry3.grid(column=1, row=2, padx=5, pady=5)
        self.boton1=ttk.Button(self.lf1, text="Crear gráfico", command=self.grafico_tarta)
        self.boton1.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky="we")
        self.entry1.focus()

    def grafico_tarta(self):
        self.canvas1.delete(tk.ALL)
        valor1=int(self.dato1.get())
        valor2=int(self.dato2.get())
        valor3=int(self.dato3.get())
        suma=valor1+valor2+valor3
        grados1=valor1/suma*360
        grados2=valor2/suma*360
        grados3=valor3/suma*360
        self.canvas1.create_arc(10,10,400,400,fill="dodgerblue", start=0, extent=grados1)
        self.canvas1.create_arc(10,10,400,400,fill="deeppink", start=grados1, extent=grados2)
        self.canvas1.create_arc(10,10,400,400,fill="green2", start=grados1+grados2, extent=grados3)        
        self.canvas1.create_text(500, 50, text="Docentes:"+str(valor1), fill="dodgerblue", font="Arial")
        self.canvas1.create_text(500, 100, text="Alumnas:"+str(valor2), fill="deeppink", font="Arial")
        self.canvas1.create_text(500, 150, text="Alumnos:"+str(valor3), fill="green2", font="Arial")
        

aplicacion1=Aplicacion()