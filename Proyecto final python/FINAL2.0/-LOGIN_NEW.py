import tkinter as tk 
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
from inicio_sesion_registro import *
from RECUPERAR_NEW import *
from REGISTRARSE_NEW_PT3 import *
class aplication7():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("LOGIN")
        self.ventana.geometry("700x600")
        self.ventana.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.ventana.rowconfigure((0), weight=1)

        # Cargar la imagen original
        self.imagen_1 = Image.open("imagenes_final2.0/nom_slogan.jpg")
        # Crear una variable global para almacenar la imagen redimensionada
        self.imagen_tk = ImageTk.PhotoImage(self.imagen_1)

        def agrandar_imagen(event):
            # Obtener el nuevo tamaño de la ventana
            self.width = event.width
            self.height = event.height
            #print(f"Nuevo tamaño: {width}x{height}")
            
            # Redimensionar la imagen con los nuevos valores de ancho y alto
            self.nueva_imagen = self.imagen_1.resize((self.width, self.height))
            self.nueva_imagen_tk = ImageTk.PhotoImage(self.nueva_imagen)
            
            # Actualizar la imagen en el canvas
            self.canva1.create_image(0, 0, image=self.nueva_imagen_tk, anchor="nw")
            
            # Necesitamos mantener la referencia a la nueva imagen para evitar que se elimine
            self.canva1.image = self.nueva_imagen_tk  # Esto es necesario para evitar que la imagen se borre

        # Funciones de los botones
        def gmail():
            print("Bienvenido a gmail, REGISTRESE")

        def inicio():
            print("Ha iniciado sesión")

        def contra():
            print("Nueva contraseña: 123ABC")

        # Cargar las imágenes de los botones
        self.imagen_google = Image.open("imagenes_final2.0/google_logo.png").resize((30, 30))
        self.imagen_google_tk = ImageTk.PhotoImage(self.imagen_google)

        self.imagen_personita = Image.open("imagenes_final2.0/personita.jpg").resize((30, 30))
        self.imagen_personita_tk = ImageTk.PhotoImage(self.imagen_personita)

        self.imagen_contra = Image.open("imagenes_final2.0/contra_logo.webp").resize((30, 30))
        self.imagen_contra_tk = ImageTk.PhotoImage(self.imagen_contra)

        # Crear el frame para los botones
        self.frame_botones = ttk.Frame(self.ventana)
        self.frame_botones.grid(column=0, row=0, sticky="nsew")

        #labels paar cada uno

        self.label_usuario=tk.Label(self.frame_botones, text="Nombre de usuario:" ,font=("Sitka Text Semibold", 20), width=500)
        self.label_usuario.pack(pady=10)

        self.entry_usuario=ctk.CTkEntry(self.frame_botones, width=300, height=30 ,fg_color="white", text_color="black")
        self.entry_usuario.pack(pady=11)

        self.label_contra=tk.Label(self.frame_botones, text="Contraseña:" ,font=("Sitka Text Semibold", 20), width=500)
        self.label_contra.pack(pady=12)

        self.entry_contra=ctk.CTkEntry(self.frame_botones, width=300, height=30 , fg_color="white", text_color="black")
        self.entry_contra.pack(pady=13)

        self.boton_persona = ttk.Button(self.frame_botones, width=50, text="INGRESAR", image=self.imagen_personita_tk, compound="left", command=self.Back_iniciar_sesion)
        self.boton_persona.pack(pady=20, padx=25)

        self.label_olvidar=tk.Label(self.frame_botones, text="¿Olvidaste tu contraseña?" ,font=("Sitka Text Semibold", 20), width=500)
        self.label_olvidar.pack(pady=21)

        self.boton_contra = ttk.Button(self.frame_botones, width=50, text="RECUPERAR", image=self.imagen_contra_tk, compound="left", command=self.boton_recuperar)
        self.boton_contra.pack(pady=22, padx=27)

        self.label_regi=tk.Label(self.frame_botones, text="¿No estás registrado?" ,font=("Sitka Text Semibold", 20), width=500)
        self.label_regi.pack(pady=23)

        self.boton_gmail = ttk.Button(self.frame_botones, width=50, text="REGISTRATE", image=self.imagen_google_tk, compound="left", command=self.boton_registrar)
        self.boton_gmail.pack(pady=24, padx=26)


        # Crear el canvas para la imagen
        self.canva1 = tk.Canvas(self.ventana, background="black")
        self.canva1.grid(column=1, row=0, columnspan=3, sticky="nsew")
        self.canva1.bind("<Configure>", agrandar_imagen)

        # Mostrar la imagen inicial (con el tamaño original)
        self.canva1.create_image(0, 0, image=self.imagen_tk, anchor="nw")

        # Ejecutar la ventana
        self.ventana.mainloop()
    def Back_iniciar_sesion(self):
    
        self.usuarios=self.entry_usuario.get()
        #self.usuarios= str(self.usuarios)
        print(self.usuarios)
        self.contraseñas=self.entry_contra.get()
        #self.contraseñas = str(self.contraseñas)
        inicio_sesion(self.usuarios,self.contraseñas)
    def boton_registrar(self):
        registracion()
    def boton_recuperar(self):
        ejecutar_recuperar_clave()
ejecutar =aplication7()