import customtkinter as ctk


from PIL import Image,ImageTk






class aplication():
    def __init__ (self):
        
        self.ventana=ctk.CTk()
        self.ventana.geometry ("800x600")
        self.frame_global =ctk.CTkFrame(self.ventana,fg_color="white")
        self.frame_global.pack(fill="both",expand=True)
        
        

        
        self.frame_imagen=ctk.CTkFrame(self.frame_global)
        self.frame_imagen.pack(fill="both",pady=(90,0))
        
        
        
        self.fondo_imagen =Image.open("D:/proyecto final kei y fer/proyecto final turnos medicos/imagenes/hospital_fondo.jpg")
        self.imagen_fondo=ImageTk.PhotoImage(self.fondo_imagen)
        self.mostrar_image_fondo=ctk.CTkLabel(self.frame_imagen,image=self.imagen_fondo)
        self.mostrar_image_fondo.pack()
        
        
        self.imagen = Image.open("D:/proyecto final kei y fer/proyecto final turnos medicos/imagenes/house.jpg")
        self.imagen = self.imagen.resize((100,100))
        self.imagentk =ImageTk.PhotoImage(self.imagen)
        
        
        self.etiqueta_imagen=ctk.CTkLabel(self.frame_imagen,image=self.imagentk)
        self.etiqueta_imagen.pack()

        self.labeluser=ctk.CTkLabel(self.frame_imagen,text="usuario: ")
        self.labeluser.pack(side="top",pady=(40,0))
        self.usuario=ctk.CTkEntry(self.frame_global)
        self.usuario.pack(side="top")
        self.labelpass=ctk.CTkLabel(self.frame_global,text="password: ")
        self.labelpass.pack(side="top")
        self.contraseña=ctk.CTkEntry(self.frame_global)
        self.contraseña.pack(side="top")
        self.boton_iniciar_sesion=ctk.CTkButton(self.frame_global,text="iniciar sesion")
        self.boton_iniciar_sesion.pack(side="top",pady=(10,10))
        self.boton_registrarse=ctk.CTkButton(self.frame_global,text="Registrarse")
        self.boton_registrarse.pack(side="top",pady=(0,10))
        self.boton_recuperar_contraseña=ctk.CTkButton(self.frame_global,text="recuperar contraseña")
        self.boton_recuperar_contraseña.pack(side="top",pady=(0,10))
        
        '''self.frame1 = ctk.CTkFrame(self.ventana,fg_color="red")
        self.frame1.pack(side="top",pady=[50,0])
        self.frame = ctk.CTkFrame(self.ventana, width=300, height=100, corner_radius=30, fg_color="green")
        self.frame.pack(padx=20, pady=20)
        self.inicio = ctk.CTkButton(self.frame1,text="inicio",command=self.modificar_grupo_familiar)
        self.inicio.pack(side="left")
        self.misturnos = ctk.CTkComboBox(self.frame1,values=["reservar turno","turnos pendientes","historial de turnos"])
        self.misturnos.pack(side="left")
        self.grupo_familiar = ctk.CTkComboBox(self.frame1,values=["titular","hijo"])
        self.grupo_familiar.pack(side="left")
        self.frame = ctk.CTkFrame(self.ventana, width=500, height=250, corner_radius=30, fg_color="blue")
        self.frame.pack(side="left",padx=20, pady=20)
        self.frame5 = ctk.CTkFrame(self.ventana, width=50, height=50, corner_radius=30, fg_color="red")
        self.frame5.pack(side="left",padx=[400,0], pady=20)

        # Agregar un botón dentro del frame
        self.label_prox_turno = ctk.CTkLabel(self.frame, text="proximo turno                     ",bg_color="green",anchor="center")
        self.label_prox_turno.pack(side="left",pady=20)
        self.label_grupo_familiar =  ctk.CTkLabel(self.frame5, text="grupo familiar                    ",bg_color="green")
        self.label_grupo_familiar.pack(side="left",pady=20,padx=[15,0])

        
        
    

        
        
        '''
        self.ventana.mainloop()
        
    def modificar_prox_turno(self):
        
        self.valor = "ronda"
        if len(self.valor) == 34:
             self.auxiliar = self.valor()
        if len(self.valor) < 34:
            self.auxiliar1 = 34-int(len(self.valor))
            self.auxiliar = self.valor+ (" "*self.auxiliar1)
            print(len(self.auxiliar))
        
        
        self.label_prox_turno.configure(text=self.auxiliar)
        
        
    def modificar_grupo_familiar(self):
        self.valor = "domda"
        if len(self.valor) == 34:
             self.auxiliar = self.valor()
        if len(self.valor) < 34:
            self.auxiliar1 = 34-int(len(self.valor))
            self.auxiliar = self.valor+ (" "*self.auxiliar1)
            print(len(self.auxiliar))
        
        
        self.label_grupo_familiar.configure(text=self.auxiliar)
        
ejecutar = aplication()