
import customtkinter as ctk
from medicos import *
class listamedicos:
    def __init__(self):
        self.ventanamedicos1=ctk.CTk()
        self.ventanamedicos1.geometry("800x600")

        self.boton_agregar_medico=ctk.CTkButton(self.ventanamedicos1,text="agregar medico",command=self.asignador_medicos_front)
        self.boton_agregar_medico.pack(side="top")
        self.boton_eliminar_medico=ctk.CTkButton(self.ventanamedicos1,text="eliminar medico",command=self.eliminador_medicos_front)
        self.boton_eliminar_medico.pack(side="top")
        self.boton_modificar_medico=ctk.CTkButton(self.ventanamedicos1,text="modificar medico",command=self.modificador_medicos_front)
        self.boton_modificar_medico.pack(side="top")
        self.ventanamedicos1.mainloop()
    
   
   
    def menu_1_medicos_asignador(self):
        self.botonmedicos2.forget()
        self.nombre_medico_label.forget()
        self.nombre_medico_entry.forget()
        self.apellido_medico_label.forget()
        self.apellido_medico_entry.forget()
        self.celular_medico_label.forget()
        self.celular_medico_entry.forget()
        self.email_medico_label.forget()
        self.email_medico_entry.forget()
        self.documentomedico_label.forget()
        self.documentomedico_entry.forget()
        self.especialidad_label.forget()
        self.especialidad_entry.forget()
        self.matricula_label.forget()
        self.matricula_entry.forget()
        self.boton_agregar_medico=ctk.CTkButton(self.ventanamedicos1,text="agregar medico",command=self.asignador_medicos_front)
        self.boton_agregar_medico.pack(side="top")
        self.boton_eliminar_medico=ctk.CTkButton(self.ventanamedicos1,text="eliminar medico",command=self.eliminador_medicos_front)
        self.boton_eliminar_medico.pack(side="top")
        self.boton_modificar_medico=ctk.CTkButton(self.ventanamedicos1,text="modificar medico",command=self.modificador_medicos_front)
        self.boton_modificar_medico.pack(side="top")
    
    def menu_2_medicos_eliminador(self):
        self.botonmedicos_eliminar2.forget()
        self.apellido_medico_eliminar_entry.forget()
        self.apellido_medico_eliminar_label.forget()
        self.nombre_medico_eliminar_entry.forget()
        self.nombre_medico_eliminar_label.forget()
        self.boton_agregar_medico.pack(side="top")
        self.boton_eliminar_medico.pack(side="top")
        self.boton_modificar_medico.pack(side="top")
    def menu_3_medicos_modificador(self):
        self.botonmedicos_modificar2.forget()
        self.boton_agregar_medico.pack(side="top")
        self.boton_eliminar_medico.pack(side="top")
        self.boton_modificar_medico.pack(side="top")
        self.documentomedico_modificar_label.forget()
        self.documentomedico_modificar_entry.forget()

        self.nombre_medico_modificar_label.forget()
        self.nombre_medico_modificar_entry.forget()
        
        self.apellido_medico_modificar_label.forget()
        self.apellido_medico_modificar_entry.forget()
        
        self.celular_medico_modificar_label.forget()
        self.celular_medico_modificar_entry.forget()
        
        self.email_medico_modificar_label.forget()
        self.email_medico_modificar_entry.forget()
        
        
       
        self.especialidad_modificar_label.forget()
        self.especialidad_modificar_entry.forget()
        
        self.matricula_modificar_label.forget()
        self.matricula_modificar_entry.forget()
        self.botonmedicos_modificar.forget()

    def asignador_medicos_front(self):
        self.boton_agregar_medico.forget()
        self.boton_eliminar_medico.forget()
        self.boton_modificar_medico.forget()
        self.nombre_medico_label=ctk.CTkLabel(self.ventanamedicos1,text="nombre_medico: ")
        self.nombre_medico_label.pack(side="top")
        self.nombre_medico_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.nombre_medico_entry.pack(side="top")
        
        self.apellido_medico_label=ctk.CTkLabel(self.ventanamedicos1,text="apellido_medico: ")
        self.apellido_medico_label.pack(side="top")
        self.apellido_medico_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.apellido_medico_entry.pack(side="top")
        
        self.celular_medico_label=ctk.CTkLabel(self.ventanamedicos1,text="celular: ")
        self.celular_medico_label.pack(side="top")
        self.celular_medico_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.celular_medico_entry.pack(side="top")
        
        self.email_medico_label=ctk.CTkLabel(self.ventanamedicos1,text="email: ")
        self.email_medico_label.pack(side="top")
        self.email_medico_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.email_medico_entry.pack(side="top")
        
        self.documentomedico_label=ctk.CTkLabel(self.ventanamedicos1,text="documento: ")
        self.documentomedico_label.pack(side="top")
        self.documentomedico_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.documentomedico_entry.pack(side="top")
       
        self.especialidad_label=ctk.CTkLabel(self.ventanamedicos1,text="especialidad: ")
        self.especialidad_label.pack(side="top")
        self.especialidad_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.especialidad_entry.pack(side="top")
        
        self.matricula_label=ctk.CTkLabel(self.ventanamedicos1,text="matricula: ")
        self.matricula_label.pack(side="top")
        self.matricula_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.matricula_entry.pack(side="top")

        self.botonmedicos=ctk.CTkButton(self.ventanamedicos1,text="aceptar",command=self.asignador_medicos_back)
        self.botonmedicos.pack(side="top")
    def asignador_medicos_back(self):
        self.botonmedicos.forget()
        self.nombres_medicos_entry=self.nombre_medico_entry.get()
        self.apellidos_medicos_entry=self.apellido_medico_entry.get()
        self.celular_medicos_entry=self.celular_medico_entry.get()
        self.email_medicos_entry=self.email_medico_entry.get()
        self.especialidads_entry=self.especialidad_entry.get()
        self.matriculass_entry=self.matricula_entry.get()
        
        nuevo_medico(self.nombres_medicos_entry,self.apellidos_medicos_entry,self.celular_medicos_entry,self.email_medicos_entry,self.email_medicos_entry,self.especialidads_entry,self.matriculass_entry)
        self.botonmedicos2=ctk.CTkButton(self.ventanamedicos1,text="volver",command=self.menu_1_medicos_asignador)
        self.botonmedicos2.pack(side="top")
    def eliminador_medicos_front(self):
        self.boton_agregar_medico.forget()
        self.boton_eliminar_medico.forget()
        self.boton_modificar_medico.forget()
        self.nombre_medico_eliminar_label=ctk.CTkLabel(self.ventanamedicos1,text="nombre_medico: ")
        self.nombre_medico_eliminar_label.pack(side="top")
        self.nombre_medico_eliminar_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.nombre_medico_eliminar_entry.pack(side="top")
        
        self.apellido_medico_eliminar_label=ctk.CTkLabel(self.ventanamedicos1,text="apellido_medico: ")
        self.apellido_medico_eliminar_label.pack(side="top")
        self.apellido_medico_eliminar_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.apellido_medico_eliminar_entry.pack(side="top")
        self.botonmedicos_eliminar=ctk.CTkButton(self.ventanamedicos1,text="aceptar",command=self.eliminador_medicos_back)
        self.botonmedicos_eliminar.pack(side="top")
    def eliminador_medicos_back(self):
        self.botonmedicos_eliminar.forget()
        self.nombres_medicos_eliminar_entry=self.nombre_medico_eliminar_entry.get()
        self.apellidos_medicos_eliminar_entry=self.apellido_medico_eliminar_entry.get()
        eliminar_medico(self.nombres_medicos_eliminar_entry,self.apellidos_medicos_eliminar_entry)
        self.botonmedicos_eliminar2=ctk.CTkButton(self.ventanamedicos1,text="volver",command=self.menu_2_medicos_eliminador)
        self.botonmedicos_eliminar2.pack(side="top")

    


    def modificador_medicos_front(self):
        self.boton_agregar_medico.forget()
        self.boton_eliminar_medico.forget()
        self.boton_modificar_medico.forget()
        self.documentomedico_modificar_label=ctk.CTkLabel(self.ventanamedicos1,text="escriba documento del medico a modificar datos: ")
        self.documentomedico_modificar_label.pack(side="top")
        self.documentomedico_modificar_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.documentomedico_modificar_entry.pack(side="top")

        self.nombre_medico_modificar_label=ctk.CTkLabel(self.ventanamedicos1,text="nombre_medico: ")
        self.nombre_medico_modificar_label.pack(side="top")
        self.nombre_medico_modificar_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.nombre_medico_modificar_entry.pack(side="top")
        
        self.apellido_medico_modificar_label=ctk.CTkLabel(self.ventanamedicos1,text="apellido_medico: ")
        self.apellido_medico_modificar_label.pack(side="top")
        self.apellido_medico_modificar_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.apellido_medico_modificar_entry.pack(side="top")
        
        self.celular_medico_modificar_label=ctk.CTkLabel(self.ventanamedicos1,text="celular: ")
        self.celular_medico_modificar_label.pack(side="top")
        self.celular_medico_modificar_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.celular_medico_modificar_entry.pack(side="top")
        
        self.email_medico_modificar_label=ctk.CTkLabel(self.ventanamedicos1,text="email: ")
        self.email_medico_modificar_label.pack(side="top")
        self.email_medico_modificar_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.email_medico_modificar_entry.pack(side="top")
        
        
       
        self.especialidad_modificar_label=ctk.CTkLabel(self.ventanamedicos1,text="especialidad: ")
        self.especialidad_modificar_label.pack(side="top")
        self.especialidad_modificar_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.especialidad_modificar_entry.pack(side="top")
        
        self.matricula_modificar_label=ctk.CTkLabel(self.ventanamedicos1,text="matricula: ")
        self.matricula_modificar_label.pack(side="top")
        self.matricula_modificar_entry=ctk.CTkEntry(self.ventanamedicos1)
        self.matricula_modificar_entry.pack(side="top")
        self.botonmedicos_modificar=ctk.CTkButton(self.ventanamedicos1,text="aceptar",command=self.modificador_medicos_back)
        self.botonmedicos_modificar.pack(side="top")
    
    def modificador_medicos_back(self):
        self.botonmedicos_modificar.forget()
        self.nombres_medicos_modificar_entry=self.nombre_medico_modificar_entry.get()
        self.apellidos_medicos_modificar_entry=self.apellido_medico_modificar_entry.get()
        self.celular_medicos_modificar_entry=self.celular_medico_modificar_entry.get()
        self.email_medicos_modificar_entry=self.email_medico_modificar_entry.get()
        self.documentomedicos_modificar_entry= self.documentomedico_modificar_entry.get()
        self.especialidad_modificars_entry=self.especialidad_modificar_entry.get()
        self.matriculasa_modificar_entry=self.matricula_modificar_entry.get()
        modificar_medico(self.nombres_medicos_modificar_entry,self.apellidos_medicos_modificar_entry,self.celular_medicos_modificar_entry,self.email_medicos_modificar_entry,self.documentomedicos_modificar_entry,self.especialidad_modificars_entry,self.matriculasa_modificar_entry)
        self.botonmedicos_modificar2=ctk.CTkButton(self.ventanamedicos1,text="volver",command=self.menu_3_medicos_modificador)
        self.botonmedicos_modificar2.pack(side="top")

ejecutar=listamedicos()
