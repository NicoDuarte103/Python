

from tkinter import *

canvas_width = 400
canvas_height = 400

colores = ("#222042", "white") 
box=[]

for ratio in ( 0.35, 0.35 ):
   box.append( (canvas_width * ratio,canvas_height * ratio,canvas_width * (1 - ratio),canvas_height * (1 - ratio) ) )
                
cuadro = Tk()

L = Canvas(cuadro, width=canvas_width, height=canvas_height)
L.pack()

for i in range(2):
   L.create_rectangle(box[i][0], box[i][1],box[i][2],box[i][3], fill=colores[i])


L.create_text(canvas_width / 2,canvas_height / 2,text="PROGRAMACION")#indica que el texto está centrado
              
              
mainloop()
