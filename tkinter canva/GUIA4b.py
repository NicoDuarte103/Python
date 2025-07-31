from tkinter import *

recuadro = Tk()

L = Canvas(recuadro, width=300, height=400,)
L.pack()

L.create_rectangle(50, 120, 250, 240, fill="#394ab8")
L.create_rectangle(70, 140, 230, 220, fill="white")


mainloop()
#------------------------------------------------------------------