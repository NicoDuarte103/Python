import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk,ImageFile
class Aplicacion:
    def __init__(self):
        self.ventana0 = ctk.CTk()  # Crear la ventana principal
        self.ventana0.title("LOGIN TURNERA")
        # Obtener las dimensiones de la pantalla y mostrra pantalla completa directamente
        self.pantalla_ancho = self.ventana0.winfo_screenwidth()
        self.pantalla_alto = self.ventana0.winfo_screenheight()
        self.ventana0.geometry(f"{self.pantalla_ancho}x{self.pantalla_alto}+0+0")
       
        
        #codigo para meter imagenes en la ventana
        self.ruta_archivo = "C:/Users/estudiante/Desktop/pillow/ejercicios/Paletas de colores/imagenpruebaparakei.jpg"
        self.imagendos=Image.open(self.ruta_archivo) #aca cambias la ruta del archivo
        self.imagentres= ImageTk.PhotoImage(self.imagendos)

        ###LABEL
        self.label=ctk.CTkLabel(self.ventana0,image=self.imagentres)
        self.label.place(x=0,y=100) 

        ###ENTRY
        #self.entry1 = ctk.CTkEntry(self.ventana0, fg_color="white",bg_color="transparent",border_color="blue", width=300) #poner un color con paleta de colores
        #self.entry1.pack(padx=250,pady=250, expand=True)#

        """###BOTON
        self.boton1=ctk.CTkButton(self.ventana0,text="boton",command=self.siguiente)
        self.boton1.place(x=200,y=200)
        
        print("hola")"""
    
      
  
        self.ventana0.mainloop()

    def siguiente(self):
        print("hola soy el siguiente")


ejecutar = Aplicacion()


#agregar los otros ejemplos

#PUNTOS A TENER EN CUENTA:

#Agregar botones y entrys que sean lo mas simetricos posibles y con el mismo 
#color que la app (blue light).

