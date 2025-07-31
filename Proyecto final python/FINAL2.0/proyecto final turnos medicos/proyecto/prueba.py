import customtkinter as ctk
from inicio_sesion_registro import *
class registro:
    def __init__(self):
        self.ventana0=ctk.CTk()
        self.ventana0.geometry("800x600")
        self.labeluser=ctk.CTkLabel(self.ventana0,text="usuario: ")
        self.labeluser.pack(side="top")
        self.usuario=ctk.CTkEntry(self.ventana0)
        self.usuario.pack(side="top")
        self.labelpass=ctk.CTkLabel(self.ventana0,text="password: ") #etiquetra
        self.labelpass.pack(side="top")
        self.contraseña=ctk.CTkEntry(self.ventana0) #entrada de texto
        self.contraseña.pack(side="top")
        self.boton_iniciar_sesion=ctk.CTkButton(self.ventana0,text="iniciar sesion")
        self.boton_iniciar_sesion.pack(side="left",padx=[100,0],pady=[0,100]) ##
        self.boton_registrarse=ctk.CTkButton(self.ventana0,text="Registrarse")
        self.boton_registrarse.pack(side="left")
        self.boton_recuperar_contraseña=ctk.CTkButton(self.ventana0,text="recuperar contraseña")
        self.boton_recuperar_contraseña.pack(side="left")

        ##padx= manejas el eje x.
        ##pady= manejas el eje y
        #ejemplo: padx= [100,0] sumas espaciose n blanco a la izquierda
        #padx= [0,100] sumas espacios en blanco a la derecha
        #pady= [100,0] sumas espacios en blanco hacia arriba
        #pady= [0,100] sumas espacios en blanco hacia abajo
        #side = "top" pone el widget arriba,si se repiten pone una cosa encima de la otra <------mas usado
        #side= "left" pone el widget a la izquierda,si se repiten ponen una cosa al lado de la otra desde la izquierda <------- mas usado
        #side = "right" pone el widget a la derecha, si se repiten ponen una cosa al lado de la otra desde la derecha
        #side = "bottm" pone el widget abajo,si se repiten ponen una cosa abajo de otra        
        
        

        self.ventana0.mainloop()
        
EJECUTAR = registro()