import customtkinter as ctk
from turnos import *
class turnos:
    def __init__(self):
        self.ventanaturnos1= ctk.CTk()
        self.ventanaturnos1.geometry("800x600")
        self.boton_agregar_turno=ctk.CTkButton(self.ventanaturnos1,text="agregar turno",command=self.asignador_turnos_front)
        self.boton_agregar_turno.pack(side="top")
        self.boton_eliminar_turno=ctk.CTkButton(self.ventanaturnos1,text="eliminar turno",command=self.eliminador_turnos_front)
        self.boton_eliminar_turno.pack(side="top")
        self.boton_modificar_turno=ctk.CTkButton(self.ventanaturnos1,text="modificar turno",command=self.modificador_turnos_front)
        self.boton_modificar_turno.pack(side="top")
        self.boton_ver_turno_cercano=ctk.CTkButton(self.ventanaturnos1,text="ver turnos cercanos",command=self.ver_turnos_cercanosfront)
        self.boton_ver_turno_cercano.pack(side="top")
        self.boton_ver_turno_viejo=ctk.CTkButton(self.ventanaturnos1,text="ver turnos viejos",command=self.ver_turnos_viejos_front)
        self.boton_ver_turno_viejo.pack(side="top")
        self.ventanaturnos1.mainloop()
    
    
    def menu_principal_turnos1(self):
        self.nombre_label.forget()
        self.nombre_entry.forget()
        self.apellido_label.forget()
        self.apellido_entry.forget()
        self.documento_label.forget()
        self.documento_entry.forget()
        self.medico_tratante_label.forget()
        self.medico_tratante_entry.forget()
        self.fecha_turno_label.forget()
        self.fecha_turno_entry.forget()
        self.hora_turno_label.forget()
        self.hora_turno_entry.forget()
        self.botonturnos2.forget()
        self.boton_agregar_turno=ctk.CTkButton(self.ventanaturnos1,text="agregar turno",command=self.asignador_turnos_front)
        self.boton_agregar_turno.pack(side="top")
        self.boton_eliminar_turno=ctk.CTkButton(self.ventanaturnos1,text="eliminar turno",command=self.eliminador_turnos_front)
        self.boton_eliminar_turno.pack(side="top")
        self.boton_modificar_turno=ctk.CTkButton(self.ventanaturnos1,text="modificar turno",command=self.modificador_turnos_front)
        self.boton_modificar_turno.pack(side="top")
        self.boton_ver_turno_cercano=ctk.CTkButton(self.ventanaturnos1,text="ver turnos cercanos",command=self.ver_turnos_cercanosfront)
        self.boton_ver_turno_cercano.pack(side="top")
        self.boton_ver_turno_viejo=ctk.CTkButton(self.ventanaturnos1,text="ver turnos viejos",command=self.ver_turnos_viejos_front)
        self.boton_ver_turno_viejo.pack(side="top")
    
    def menu_principal_turnos2(self):
        self.documento_eliminar_turno_label.forget()
        self.documento_eliminar_turno_entry.forget()
        self.boton_eliminar_turnos2.forget()
        self.boton_agregar_turno.pack(side="top")
        self.boton_eliminar_turno.pack(side="top")
        self.boton_modificar_turno.pack(side="top")
        self.boton_ver_turno_cercano.pack(side="top")
    def menu_principal_turnos3(self):
        self.boton_agregar_turno.pack(side="top")
        self.boton_eliminar_turno.pack(side="top")
        self.boton_modificar_turno.pack(side="top")
        self.boton_ver_turno_cercano.pack(side="top")
        self.fecha_a_modificar_label.forget()
        self.fecha_a_modificar_turno_entry.forget()
        self.horario_a_modificar_label.forget()
        self.horario_a_modificar_turno_entry.forget()
        self.boton_modificar_turnos2.forget()
        self.documento_fecha_y_hora_a_modificar_label.forget()
        self.documento_fecha_y_hora_a_modificar_entry.forget()
    def menu_principal_turnos4(self):

        self.boton_agregar_turno.pack(side="top")
        self.boton_eliminar_turno.pack(side="top")
        self.boton_modificar_turno.pack(side="top")
        self.boton_ver_turno_cercano.pack(side="top")
        self.boton_turno_pendiente2.forget()
        self.documento_turno_pendiente_label.forget()
        self.documento_turno_pendiente_entry.forget()
    
    def menu_principal_turnos5(self):

        self.boton_agregar_turno.pack(side="top")
        self.boton_eliminar_turno.pack(side="top")
        self.boton_modificar_turno.pack(side="top")
        self.boton_ver_turno_cercano.pack(side="top")
        self.boton_turno_viejo2.forget()
        self.documento_turno_viejo_label.forget()
        self.documento_turno_viejo_entry.forget()
        
    def asignador_turnos_front(self):
        self.boton_agregar_turno.forget()
        self.boton_eliminar_turno.forget()
        self.boton_modificar_turno.forget()
        self.nombre_label=ctk.CTkLabel(self.ventanaturnos1,text="Nombre: ")
        self.nombre_label.pack(side="top")
        self.nombre_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.nombre_entry.pack(side="top")
        
        self.apellido_label=ctk.CTkLabel(self.ventanaturnos1,text="apellido: ")
        self.apellido_label.pack(side="top")
        self.apellido_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.apellido_entry.pack(side="top")
        
        self.documento_label=ctk.CTkLabel(self.ventanaturnos1,text="documento: ")
        self.documento_label.pack(side="top")
        self.documento_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.documento_entry.pack(side="top")
        
        self.obra_socialnro_label=ctk.CTkLabel(self.ventanaturnos1,text="obra socialnro: ")
        self.obra_socialnro_label.pack(side="top")
        self.obra_socialnro_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.obra_socialnro_entry.pack(side="top")
        
        self.especialidad_medica_label=ctk.CTkLabel(self.ventanaturnos1,text="especialidad medica: ")
        self.especialidad_medica_label.pack(side="top")
        self.especialidad_medica_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.especialidad_medica_entry.pack(side="top")

        
        self.medico_tratante_label=ctk.CTkLabel(self.ventanaturnos1,text="medico tratante: ")
        self.medico_tratante_label.pack(side="top")
        self.medico_tratante_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.medico_tratante_entry.pack(side="top")
        
        
        self.fecha_turno_label=ctk.CTkLabel(self.ventanaturnos1,text="fecha turno:: ")
        self.fecha_turno_label.pack(side="top")
        self.fecha_turno_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.fecha_turno_entry.pack(side="top")
       
        self.hora_turno_label=ctk.CTkLabel(self.ventanaturnos1,text="hora: ")
        self.hora_turno_label.pack(side="top")
        self.hora_turno_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.hora_turno_entry.pack(side="top")

        self.botonturnos=ctk.CTkButton(self.ventanaturnos1,text="aceptar",command=self.asignador_turnos_back)
        self.botonturnos.pack(side="top")
    def asignador_turnos_back(self):
        self.botonturnos.forget()
        self.nombres_entry=self.nombre_entry.get()
        self.apellidos_entry=self.apellido_entry.get()
        self.documentos_entry=self.documento_entry.get()
        self.medicos_tratantes_entry=self.medico_tratante_entry.get()
        self.fechas_turnos_entry=self.fecha_turno_entry.get()
        self.horas_turnos_entry=self.hora_turno_entry.get()
        asignar_turno(self.nombres_entry,self.apellidos_entry,self.documentos_entry,self.medicos_tratantes_entry,self.fechas_turnos_entry,self.horas_turnos_entry)
        self.botonturnos2=ctk.CTkButton(self.ventanaturnos1,text="volver",command=self.menu_principal_turnos1)
        self.botonturnos2.pack(side="top")
    
    def eliminador_turnos_front(self):
        self.boton_agregar_turno.forget()
        self.boton_eliminar_turno.forget()
        self.boton_modificar_turno.forget()
        self.documento_eliminar_turno_label=ctk.CTkLabel(self.ventanaturnos1,text="documentoa eliminar turno: ")
        self.documento_eliminar_turno_label.pack(side="top")
        self.documento_eliminar_turno_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.documento_eliminar_turno_entry.pack(side="top")
        
        self.fecha_turno_eliminar_label=ctk.CTkLabel(self.ventanaturnos1,text="fecha de turno a eliminar: ")
        self.fecha_turno_eliminar_label.pack(side="top")
        self.fecha_turno_eliminar_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.fecha_turno_eliminar_entry.pack(side="top")
        self.boton_eliminar_turnos=ctk.CTkButton(self.ventanaturnos1,text="aceptar",command=self.eliminador_turnos_back)
        self.boton_eliminar_turnos.pack(side="top")
    def eliminador_turnos_back(self):

        self.documentos_eliminar_turnos_entry=self.documento_eliminar_turno_entry.get()
        borrar_turno(self.documentos_eliminar_turnos_entry)
        self.boton_eliminar_turnos.forget()
        self.boton_eliminar_turnos2=ctk.CTkButton(self.ventanaturnos1,text="volver",command=self.menu_principal_turnos2)
        self.boton_eliminar_turnos2.pack(side="top")
    def modificador_turnos_front(self):
        self.boton_agregar_turno.forget()
        self.boton_eliminar_turno.forget()
        self.boton_modificar_turno.forget()
        
        self.documento_fecha_y_hora_a_modificar_label=ctk.CTkLabel(self.ventanaturnos1,text="documento: ")
        self.documento_fecha_y_hora_a_modificar_label.pack(side="top")
        self.documento_fecha_y_hora_a_modificar_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.documento_fecha_y_hora_a_modificar_entry.pack(side="top")

        self.fecha_a_modificar_label=ctk.CTkLabel(self.ventanaturnos1,text="fecha a modificar: ")
        self.fecha_a_modificar_label.pack(side="top")
        self.fecha_a_modificar_turno_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.fecha_a_modificar_turno_entry.pack(side="top")

        self.horario_a_modificar_label=ctk.CTkLabel(self.ventanaturnos1,text="horario a modificar: ")
        self.horario_a_modificar_label.pack(side="top")
        self.horario_a_modificar_turno_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.horario_a_modificar_turno_entry.pack(side="top")



        self.boton_modificar_turnos=ctk.CTkButton(self.ventanaturnos1,text="aceptar",command=self.modificador_turnos_back)
        self.boton_modificar_turnos.pack(side="top")

    def modificador_turnos_back(self):
        self.boton_modificar_turnos.forget()
        self.documentos_fechas_y_horas_a_modificar_entry=self.documento_fecha_y_hora_a_modificar_entry.get()
        self.fechas_a_modificar_turnos_entry=self.fecha_a_modificar_turno_entry.get()
        self.horarios_a_modificar_turno_entry=self.horario_a_modificar_turno_entry.get()
        modificar_turno(self.fechas_a_modificar_turnos_entry,self.horarios_a_modificar_turno_entry,self.documentos_fechas_y_horas_a_modificar_entry)
        self.boton_modificar_turnos2=ctk.CTkButton(self.ventanaturnos1,text="volver",command=self.menu_principal_turnos3)
        self.boton_modificar_turnos2.pack(side="top")
    def ver_turnos_cercanosfront(self):
        self.boton_agregar_turno.forget()
        self.boton_eliminar_turno.forget()
        self.boton_modificar_turno.forget()
        self.boton_ver_turno_cercano.forget()
        self.documento_turno_pendiente_label=ctk.CTkLabel(self.ventanaturnos1,text="documento: ")
        self.documento_turno_pendiente_label.pack(side="top")
        self.documento_turno_pendiente_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.documento_turno_pendiente_entry.pack(side="top")
        self.boton_turno_pendiente=ctk.CTkButton(self.ventanaturnos1,text="aceptar",command=self.ver_turnos_cercanosback)
        self.boton_turno_pendiente.pack(side="top")
        
    def ver_turnos_cercanosback(self):
        self.boton_turno_pendiente.forget()
        self.documentos_turnos_pendientes_entry=self.documento_turno_pendiente_entry.get()
        ver_turnos_pendientes(self.documentos_turnos_pendientes_entry)
        self.boton_turno_pendiente2=ctk.CTkButton(self.ventanaturnos1,text="volver",command=self.menu_principal_turnos4)
        self.boton_turno_pendiente2.pack(side="top")
    def ver_turnos_viejos_front(self):
        self.boton_agregar_turno.forget()
        self.boton_eliminar_turno.forget()
        self.boton_modificar_turno.forget()
        self.boton_ver_turno_cercano.forget()
        self.boton_ver_turno_viejo.forget()
        self.documento_turno_viejo_label=ctk.CTkLabel(self.ventanaturnos1,text="documento: ")
        self.documento_turno_viejo_label.pack(side="top")
        self.documento_turno_viejo_entry=ctk.CTkEntry(self.ventanaturnos1)
        self.documento_turno_viejo_entry.pack(side="top")
        self.boton_turno_viejo=ctk.CTkButton(self.ventanaturnos1,text="aceptar",command=self.ver_turnos_viejos_back)
        self.boton_turno_viejo.pack(side="top")
    def ver_turnos_viejos_back(self):
        self.boton_turno_viejo.forget()
        self.documentos_turnos_viejos_entry=self.documento_turno_viejo_entry.get()
        ver_historial_turnos(self.documentos_turnos_viejos_entry)
        
        self.boton_turno_viejo2=ctk.CTkButton(self.ventanaturnos1,text="volver",command=self.menu_principal_turnos5)
        self.boton_turno_viejo2.pack(side="top")

ejecutar=turnos()