from tkinter import *
from tkinter import messagebox
 
 
class MiCalculadora(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.crearWidgets()
 
    def suprUltimoCaracter(self):
        Longtexto = len(self.display.get())
 
        if Longtexto >= 1:
            self.display.delete(Longtexto - 1, END)
        if Longtexto == 1:
            self.remplazarTexto("0")
 
    def remplazarTexto(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)
 
    def append(self, text):
        actualText = self.display.get()
        Longtexto = len(actualText)
        if actualText == "0":
            self.remplazarTexto(text)
        else:
            self.display.insert(Longtexto, text)
 
    def evaluar(self):
        try:
            self.remplazarTexto(eval(self.display.get()))
        except (SyntaxError, AttributeError):
            messagebox.mostrarError("Error", "Syntax Error")
            self.remplazarTexto("0")
        except ZeroDivisionError:
            messagebox.mostrarError("Error", "No es posible dividir por 0")
            self.remplazarTexto("0")
    def cajaSignos(self):
        ListOperaciones = ["*", "/", "+", "-"]
        display = self.display.get()
        for c in display:
            if c in ListOperaciones:
                 return True
        return False
 
    def cambioSignos(self):
        if self.cajaSignos():
            self.evaluar()
        PrimerCaracter = self.display.get()[0]
        if PrimerCaracter == "0":
            pass
        elif PrimerCaracter == "-":
            self.display.delete(0)
        else:
            self.display.insert(0, "-")
    def inverso(self):
        self.display.insert(0, "1/(")
        self.append(")")
        self.evaluar()
 
    def crearWidgets(self):
        self.display = Entry(self, font=("Arial", 24), relief=RAISED, justify=RIGHT, bg='darkblue', fg='white', borderwidth=0)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")
 
        self.botonCe = Button(self, font=("Arial", 12), fg='blue', text="CE", highlightbackground='blue', command=lambda: self.remplazarTexto("0"))
        self.botonCe.grid(row=1, column=0, sticky="nsew")
        self.botonInversa = Button(self, font=("Arial", 12), fg='blue', text="1/x", highlightbackground='lightgrey', command=lambda: self.inverso())
        self.botonInversa.grid(row=1, column=2, sticky="nsew")
        self.botonsupr = Button(self, font=("Arial", 12), fg='blue', text="Del", highlightbackground='blue', command=lambda: self.suprUltimoCaracter())
        self.botonsupr.grid(row=1, column=1, sticky="nsew")
        self.botonDiv = Button(self, font=("Arial", 12), fg='blue', text="/", highlightbackground='lightgrey', command=lambda: self.append("/"))
        self.botonDiv.grid(row=1, column=3, sticky="nsew")
 
        self.botonSiete = Button(self, font=("Arial", 12), fg='black', text="7", highlightbackground='black', command=lambda: self.append("7"))
        self.botonSiete.grid(row=2, column=0, sticky="nsew")
        self.botonOcho = Button(self, font=("Arial", 12), fg='black', text="8", highlightbackground='black', command=lambda: self.append("8"))
        self.botonOcho.grid(row=2, column=1, sticky="nsew")
        self.botonNueve = Button(self, font=("Arial", 12), fg='black', text="9", highlightbackground='black', command=lambda: self.append("9"))
        self.botonNueve.grid(row=2, column=2, sticky="nsew")
        self.botonMult = Button(self, font=("Arial", 12), fg='blue', text="*", highlightbackground='lightgrey', command=lambda: self.append("*"))
        self.botonMult.grid(row=2, column=3, sticky="nsew")
 
        self.botoncuatro = Button(self, font=("Arial", 12), fg='black', text="4", highlightbackground='black', command=lambda: self.append("4"))
        self.botoncuatro.grid(row=3, column=0, sticky="nsew")
        self.botoncinco = Button(self, font=("Arial", 12), fg='black', text="5", highlightbackground='black', command=lambda: self.append("5"))
        self.botoncinco.grid(row=3, column=1, sticky="nsew")
        self.botonseis = Button(self, font=("Arial", 12), fg='black', text="6", highlightbackground='black', command=lambda: self.append("6"))
        self.botonseis.grid(row=3, column=2, sticky="nsew")
        self.botonMenos = Button(self, font=("Arial", 12), fg='blue', text="-", highlightbackground='lightgrey', command=lambda: self.append("-"))
        self.botonMenos.grid(row=3, column=3, sticky="nsew")
 
        self.botonUno = Button(self, font=("Arial", 12), fg='black', text="1", highlightbackground='black', command=lambda: self.append("1"))
        self.botonUno.grid(row=4, column=0, sticky="nsew")
        self.botonDos = Button(self, font=("Arial", 12), fg='black', text="2", highlightbackground='black', command=lambda: self.append("2"))
        self.botonDos.grid(row=4, column=1, sticky="nsew")
        self.botonTres = Button(self, font=("Arial", 12), fg='black', text="3", highlightbackground='black', command=lambda: self.append("3"))
        self.botonTres.grid(row=4, column=2, sticky="nsew")
        self.botonsuma = Button(self, font=("Arial", 12), fg='blue', text="+", highlightbackground='lightgrey', command=lambda: self.append("+"))
        self.botonsuma.grid(row=4, column=3, sticky="nsew")
 
        self.botonModifNeg = Button(self, font=("Arial", 12), fg='blue', text="+/-", highlightbackground='lightgrey', command=lambda: self.cambioSignos())
        self.botonModifNeg .grid(row=5, column=0, sticky="nsew")
        self.botonCero = Button(self, font=("Arial", 12), fg='black', text="0", highlightbackground='black', command=lambda: self.append("0"))
        self.botonCero.grid(row=5, column=1, sticky="nsew")
        self.BotonDecimal = Button(self, font=("Arial", 12), fg='blue', text=".", highlightbackground='lightgrey', command=lambda: self.append("."))
        self.BotonDecimal.grid(row=5, column=2, sticky="nsew")
        self.botonIgual = Button(self, font=("Arial", 12), fg='blue', text="=", highlightbackground='lightgrey', command=lambda: self.evaluar())
        self.botonIgual.grid(row=5, column=3, sticky="nsew")
Calculador = Tk()
Calculador.title("Calculadora")
Calculador.resizable(False, False)
Calculador.config(cursor="clock")
root = MiCalculadora(Calculador).grid()
Calculador.mainloop()