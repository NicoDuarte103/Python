import tkinter as tk 
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
from inicio_sesion_registro import *
from RECUPERAR_NEW_PT4 import *

class aplication11():

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("NUEVA CONTRASEÑA")
        self.ventana.geometry("700x600")
        self.ventana.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.ventana.rowconfigure((0), weight=1)

        # Cargar la imagen original
        #self.imagen_1 = Image.open("imagenes_final2.0/logo.jpg")
        # Crear una variable global para almacenar la imagen redimensionada
        #self.imagen_tk = ImageTk.PhotoImage(self.imagen_1)
        

        def agrandar_imagen(event):
            # Obtener el nuevo tamaño de la ventana
            self.width = event.width
            self.height = event.height
            #print(f"Nuevo tamaño: {width}x{height}")
            
            # Redimensionar la imagen con los nuevos valores de ancho y alto
            #self.nueva_imagen = self.imagen_1.resize((self.width, self.height))
            #self.nueva_imagen_tk = ImageTk.PhotoImage(self.nueva_imagen)
            
            # Actualizar la imagen en el canvas
            #self.canva1.create_image(0, 0, image=self.nueva_imagen_tk, anchor="nw")
            
            # Necesitamos mantener la referencia a la nueva imagen para evitar que se elimine
            #self.canva1.image = self.nueva_imagen_tk  # Esto es necesario para evitar que la imagen se borre

        #funcion para boton confirmar
        def contra():
            print("Nueva contraseña: 123ABC")


        #self.imagen_contra = Image.open("imagenes_final2.0/contra_logo.webp").resize((30, 30))
        #self.imagen_contra_tk = ImageTk.PhotoImage(self.imagen_contra)

        # Crear el frame para los botones
        self.frame = ttk.Frame(self.ventana)
        self.frame.grid(column=0, row=0, sticky="nsew")

        #labels paar cada uno

        self.label_reasig=tk.Label(self.frame, text="Reasignación:" ,font=("Sitka Text Semibold", 30), width=500)
        self.label_reasig.pack(pady=9)

        self.label_dni=tk.Label(self.frame, text="Ingrese DNI:" ,font=("Sitka Text Semibold", 20), width=500)
        self.label_dni.pack(pady=10)

        self.entry_dni=ctk.CTkEntry(self.frame, width=300, height=30 ,fg_color="white", text_color="black")
        self.entry_dni.pack(pady=11)

        self.label_contra=tk.Label(self.frame, text="Contraseña nueva:" ,font=("Sitka Text Semibold", 20), width=500)
        self.label_contra.pack(pady=12)

        self.entry_contra=ctk.CTkEntry(self.frame, width=300, height=30 , fg_color="white", text_color="black")
        self.entry_contra.pack(pady=13)

        self.boton_confir = ttk.Button(self.frame, width=50, text="CONFIRMAR", compound="left", command=self.subir_nueva_contraseña)
        self.boton_confir.pack(pady=15, padx=27)

        #self.label_aviso=tk.Label(self.frame, text="Enviaremos un Mail a\n tu cuenta con la nueva\n contraseña de usuario\n que te asignamos." ,font=("Sitka Text Semibold", 20), width=500)
        #self.label_aviso.pack(pady=18)


        # Crear el canvas para la imagen
        #self.canva1 = tk.Canvas(self.ventana, background="black")
       #self.canva1.grid(column=1, row=0, columnspan=3, sticky="nsew")
        #self.canva1.bind("<Configure>", agrandar_imagen)

        # Mostrar la imagen inicial (con el tamaño original)
        #self.canva1.create_image(0, 0, image=self.imagen_tk, anchor="nw")

        # Ejecutar la ventana
        self.ventana.mainloop()

    
        

    def subir_nueva_contraseña(self):
        self.documentos_recuperar_contraseñas = self.entry_dni.get()
        self.contraseñas_recuperar_entry = self.entry_contra.get()
        cambiar_contraseña(self.documentos_recuperar_contraseñas,self.contraseñas_recuperar_entry)
        self.ventana.destroy()
        confirmar_recuperacion_clave()
        

def ejecutar_recuperar_clave():
    ejecutar=aplication11()