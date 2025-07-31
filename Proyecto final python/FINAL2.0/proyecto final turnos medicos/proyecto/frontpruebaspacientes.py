
import customtkinter as ctk
from pacientes import *
class listapacientes:
    def __init__(self):
        self.ventanapacientes1=ctk.CTk()
        self.ventanapacientes1.geometry("800x600")

        self.boton_agregar_paciente=ctk.CTkButton(self.ventanapacientes1,text="agregar paciente",command=self.asignador_pacientes_front)
        self.boton_agregar_paciente.pack(side="top")
        self.boton_eliminar_paciente=ctk.CTkButton(self.ventanapacientes1,text="eliminar paciente",command=self.eliminador_pacientes_front)
        self.boton_eliminar_paciente.pack(side="top")
        self.boton_modificar_paciente=ctk.CTkButton(self.ventanapacientes1,text="modificar paciente",command=self.modificador_pacientes_front)
        self.boton_modificar_paciente.pack(side="top")
        self.ventanapacientes1.mainloop()
    
   
   
    def menu_1_pacientes_asignador(self):
        self.botonpacientes2.forget()
        self.nombre_paciente_label.forget()
        self.nombre_paciente_entry.forget()
        self.apellido_paciente_label.forget()
        self.apellido_paciente_entry.forget()
        self.celular_paciente_label.forget()
        self.celular_paciente_entry.forget()
        self.email_paciente_label.forget()
        self.email_paciente_entry.forget()
        self.documentopaciente_label.forget()
        self.documentopaciente_entry.forget()
        self.obra_social_label.forget()
        self.obra_social_entry.forget()
        
        self.boton_agregar_paciente=ctk.CTkButton(self.ventanapacientes1,text="agregar paciente",command=self.asignador_pacientes_front)
        self.boton_agregar_paciente.pack(side="top")
        self.boton_eliminar_paciente=ctk.CTkButton(self.ventanapacientes1,text="eliminar paciente",command=self.eliminador_pacientes_front)
        self.boton_eliminar_paciente.pack(side="top")
        self.boton_modificar_paciente=ctk.CTkButton(self.ventanapacientes1,text="modificar paciente",command=self.modificador_pacientes_front)
        self.boton_modificar_paciente.pack(side="top")
    
    def menu_2_pacientes_eliminador(self):
        self.botonpacientes_eliminar2.forget()
        self.apellido_paciente_eliminar_entry.forget()
        self.apellido_paciente_eliminar_label.forget()
        self.nombre_paciente_eliminar_entry.forget()
        self.nombre_paciente_eliminar_label.forget()
        self.boton_agregar_paciente.pack(side="top")
        self.boton_eliminar_paciente.pack(side="top")
        self.boton_modificar_paciente.pack(side="top")
    def menu_3_pacientes_modificador(self):
        self.botonpacientes_modificar2.forget()
        self.boton_agregar_paciente.pack(side="top")
        self.boton_eliminar_paciente.pack(side="top")
        self.boton_modificar_paciente.pack(side="top")
        self.documentopaciente_modificar_label.forget()
        self.documentopaciente_modificar_entry.forget()

        self.nombre_paciente_modificar_label.forget()
        self.nombre_paciente_modificar_entry.forget()
        
        self.apellido_paciente_modificar_label.forget()
        self.apellido_paciente_modificar_entry.forget()
        
        self.celular_paciente_modificar_label.forget()
        self.celular_paciente_modificar_entry.forget()
        
        self.email_paciente_modificar_label.forget()
        self.email_paciente_modificar_entry.forget()
        
        
       
        self.obra_social_modificar_label.forget()
        self.obra_social_modificar_entry.forget()
        
   
        self.botonpacientes_modificar.forget()

    def asignador_pacientes_front(self):
        self.boton_agregar_paciente.forget()
        self.boton_eliminar_paciente.forget()
        self.boton_modificar_paciente.forget()
        self.nombre_paciente_label=ctk.CTkLabel(self.ventanapacientes1,text="nombre_paciente: ")
        self.nombre_paciente_label.pack(side="top")
        self.nombre_paciente_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.nombre_paciente_entry.pack(side="top")
        
        self.apellido_paciente_label=ctk.CTkLabel(self.ventanapacientes1,text="apellido_paciente: ")
        self.apellido_paciente_label.pack(side="top")
        self.apellido_paciente_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.apellido_paciente_entry.pack(side="top")
        
        self.celular_paciente_label=ctk.CTkLabel(self.ventanapacientes1,text="celular: ")
        self.celular_paciente_label.pack(side="top")
        self.celular_paciente_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.celular_paciente_entry.pack(side="top")
        
        self.email_paciente_label=ctk.CTkLabel(self.ventanapacientes1,text="email: ")
        self.email_paciente_label.pack(side="top")
        self.email_paciente_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.email_paciente_entry.pack(side="top")
        
        self.documentopaciente_label=ctk.CTkLabel(self.ventanapacientes1,text="documento: ")
        self.documentopaciente_label.pack(side="top")
        self.documentopaciente_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.documentopaciente_entry.pack(side="top")
       
        self.obra_social_label=ctk.CTkLabel(self.ventanapacientes1,text="obra_social: ")
        self.obra_social_label.pack(side="top")
        self.obra_social_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.obra_social_entry.pack(side="top")
        

        self.botonpacientes=ctk.CTkButton(self.ventanapacientes1,text="aceptar",command=self.asignador_pacientes_back)
        self.botonpacientes.pack(side="top")
    def asignador_pacientes_back(self):
        self.botonpacientes.forget()
        self.nombres_pacientes_entry=self.nombre_paciente_entry.get()
        self.apellidos_pacientes_entry=self.apellido_paciente_entry.get()
        self.celular_pacientes_entry=self.celular_paciente_entry.get()
        self.email_pacientes_entry=self.email_paciente_entry.get()
        self.obra_socials_entry=self.obra_social_entry.get()
      
        
        nuevo_paciente(self.nombres_pacientes_entry,self.apellidos_pacientes_entry,self.celular_pacientes_entry,self.email_pacientes_entry,self.email_pacientes_entry,self.obra_socials_entry)
        self.botonpacientes2=ctk.CTkButton(self.ventanapacientes1,text="volver",command=self.menu_1_pacientes_asignador)
        self.botonpacientes2.pack(side="top")
    def eliminador_pacientes_front(self):
        self.boton_agregar_paciente.forget()
        self.boton_eliminar_paciente.forget()
        self.boton_modificar_paciente.forget()
        self.nombre_paciente_eliminar_label=ctk.CTkLabel(self.ventanapacientes1,text="nombre_paciente: ")
        self.nombre_paciente_eliminar_label.pack(side="top")
        self.nombre_paciente_eliminar_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.nombre_paciente_eliminar_entry.pack(side="top")
        
        self.apellido_paciente_eliminar_label=ctk.CTkLabel(self.ventanapacientes1,text="apellido_paciente: ")
        self.apellido_paciente_eliminar_label.pack(side="top")
        self.apellido_paciente_eliminar_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.apellido_paciente_eliminar_entry.pack(side="top")
        self.botonpacientes_eliminar=ctk.CTkButton(self.ventanapacientes1,text="aceptar",command=self.eliminador_pacientes_back)
        self.botonpacientes_eliminar.pack(side="top")
    def eliminador_pacientes_back(self):
        self.botonpacientes_eliminar.forget()
        self.nombres_pacientes_eliminar_entry=self.nombre_paciente_eliminar_entry.get()
        self.apellidos_pacientes_eliminar_entry=self.apellido_paciente_eliminar_entry.get()
        eliminar_paciente(self.nombres_pacientes_eliminar_entry,self.apellidos_pacientes_eliminar_entry)
        self.botonpacientes_eliminar2=ctk.CTkButton(self.ventanapacientes1,text="volver",command=self.menu_2_pacientes_eliminador)
        self.botonpacientes_eliminar2.pack(side="top")

    


    def modificador_pacientes_front(self):
        self.boton_agregar_paciente.forget()
        self.boton_eliminar_paciente.forget()
        self.boton_modificar_paciente.forget()
        self.documentopaciente_modificar_label=ctk.CTkLabel(self.ventanapacientes1,text="escriba documento del paciente a modificar datos: ")
        self.documentopaciente_modificar_label.pack(side="top")
        self.documentopaciente_modificar_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.documentopaciente_modificar_entry.pack(side="top")

        self.nombre_paciente_modificar_label=ctk.CTkLabel(self.ventanapacientes1,text="nombre_paciente: ")
        self.nombre_paciente_modificar_label.pack(side="top")
        self.nombre_paciente_modificar_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.nombre_paciente_modificar_entry.pack(side="top")
        
        self.apellido_paciente_modificar_label=ctk.CTkLabel(self.ventanapacientes1,text="apellido_paciente: ")
        self.apellido_paciente_modificar_label.pack(side="top")
        self.apellido_paciente_modificar_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.apellido_paciente_modificar_entry.pack(side="top")
        
        self.celular_paciente_modificar_label=ctk.CTkLabel(self.ventanapacientes1,text="celular: ")
        self.celular_paciente_modificar_label.pack(side="top")
        self.celular_paciente_modificar_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.celular_paciente_modificar_entry.pack(side="top")
        
        self.email_paciente_modificar_label=ctk.CTkLabel(self.ventanapacientes1,text="email: ")
        self.email_paciente_modificar_label.pack(side="top")
        self.email_paciente_modificar_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.email_paciente_modificar_entry.pack(side="top")
        
        
       
        self.obra_social_modificar_label=ctk.CTkLabel(self.ventanapacientes1,text="obra_social: ")
        self.obra_social_modificar_label.pack(side="top")
        self.obra_social_modificar_entry=ctk.CTkEntry(self.ventanapacientes1)
        self.obra_social_modificar_entry.pack(side="top")
        
        
        self.botonpacientes_modificar=ctk.CTkButton(self.ventanapacientes1,text="aceptar",command=self.modificador_pacientes_back)
        self.botonpacientes_modificar.pack(side="top")
    
    def modificador_pacientes_back(self):
        self.botonpacientes_modificar.forget()
        self.nombres_pacientes_modificar_entry=self.nombre_paciente_modificar_entry.get()
        self.apellidos_pacientes_modificar_entry=self.apellido_paciente_modificar_entry.get()
        self.celular_pacientes_modificar_entry=self.celular_paciente_modificar_entry.get()
        self.email_pacientes_modificar_entry=self.email_paciente_modificar_entry.get()
        self.documentopacientes_modificar_entry= self.documentopaciente_modificar_entry.get()
        self.obra_social_modificars_entry=self.obra_social_modificar_entry.get()
        modificar_paciente(self.nombres_pacientes_modificar_entry,self.apellidos_pacientes_modificar_entry,self.celular_pacientes_modificar_entry,self.email_pacientes_modificar_entry,self.documentopacientes_modificar_entry,self.obra_social_modificars_entry)
        self.botonpacientes_modificar2=ctk.CTkButton(self.ventanapacientes1,text="volver",command=self.menu_3_pacientes_modificador)
        self.botonpacientes_modificar2.pack(side="top")

ejecutar=listapacientes()
