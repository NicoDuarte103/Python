import sqlite3 as sql

def conexion():
    conn= sql.connect("turnos.db")
    cursor=conn.cursor()
    instruccion="""CREATE TABLE IF NOT EXISTS turnos (
                                                            nombre text,
                                                            documento INTEGER,
                                                            medico_tratante text,
                                                            fecha_turno DATE,
                                                            hora_turno TIME)"""
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def asignar_turno(nombre,documento,medico_tratante,fecha_turno,hora_turno):
    conn= sql.connect("turnos.db")
    cursor=conn.cursor()
    instruccion=f"INSERT INTO turnos VALUES ('{nombre}',{documento},'{medico_tratante}','{fecha_turno}','{hora_turno}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
def borrar_turno(documento):
    conn= sql.connect("turnos.db")
    cursor=conn.cursor()
    instruccion=f"DELETE FROM turnos WHERE documento={documento}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close
def modificar_turno(nueva_fecha,nueva_hora,documento):
   # nueva_fecha =input("seleccione nueva fecha:")
   # nueva_hora= input("seleccione nueva hora: ")
    conn= sql.connect("turnos.db")
    cursor=conn.cursor()
    instruccion1=f"UPDATE turnos SET fecha_turno='{nueva_fecha}' WHERE documento={documento}"
    instruccion2=f"UPDATE turnos SET hora_turno='{nueva_hora}' WHERE documento={documento}"
    cursor.execute(instruccion1)
    conn.commit()
    cursor.execute(instruccion2)
    conn.commit()
    conn.close()
def ver_turnos_pendientes(documento):
    conn= sql.connect("turnos.db")
    cursor=conn.cursor()
    instruccion=f"SELECT * FROM turnos WHERE documento={documento} AND fecha_turno > CURRENT_DATE"
    cursor.execute(instruccion)
    dato=cursor.fetchall()
    conn.commit()
    conn.close()
    print(dato)

def ver_historial_turnos(documento):
    conn= sql.connect("turnos.db")
    cursor=conn.cursor()
    instruccion=f"SELECT * FROM turnos WHERE documento={documento} AND fecha_turno < CURRENT_DATE"
    cursor.execute(instruccion)
    dato=cursor.fetchall()
    conn.commit()
    conn.close()
    print(dato)
conexion()
if __name__=="__main__":
    conexion()
    selector=int(input("1-asignar turno \n 2-borrar turno 3-modificar turno\n 4-ver turnos pendientes\n 5-ver historial turnos\n"))
    match(selector):
        case 1:
            nombre=input("ingrese nombre: ")
            apellido=input("ingrese apellido: ")
            documento=int(input("ingrese documento: "))
            medico_tratante= input("ingrese medico: ")
            fecha=input("ingrese fecha: ")
            hora=input("ingrese hora: ")
            asignar_turno(nombre,apellido,documento,medico_tratante,fecha,hora)
        case 2:
            documento=int(input("ingrese documento a borrar turno"))
            borrar_turno(documento)
        case 3:
            documento=int(input("ingrese documento a modificar turno"))
            modificar_turno(documento)
        case 4:
            documento=int(input("escriba documento: "))
            ver_turnos_pendientes(documento)
        case 5:
            documento=int(input("escriba documento: "))
            ver_historial_turnos(documento)
        
