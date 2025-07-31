import sqlite3 as sql

def conexion():
    conn=sql.connect("pacientes.db")
    cursor=conn.cursor()
    instruccion= """CREATE TABLE IF NOT EXISTS pacientes(
                                            nombre text,
                                            apellido text,
                                            celular text,
                                            email text,
                                            documento integer,
                                            obra_social integer)"""
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def nuevo_paciente(nombre,apellido,celular,email,documento,obra_social):
    conn=sql.connect("pacientes.db")
    cursor=conn.cursor()
    instruccion=f"INSERT INTO pacientes VALUES('{nombre}','{apellido}','{celular}','{email}',{documento},{obra_social})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def eliminar_paciente(nombre,apellido):
    conn=sql.connect("pacientes.db")
    cursor=conn.cursor()
    instruccion=f"DELETE FROM pacientes WHERE nombre='{nombre}' and apellido='{apellido}'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    print(f"nombre: {nombre},{apellido} eliminado")

def modificar_paciente(nombre,apellido,celular,email,documento,obra_social):
    conn=sql.connect("pacientes.db")
    cursor=conn.cursor()
    if __name__ == "__main__":
        selector=int(input("que desea modificar \n 1-nombre \n 2-apellido \n 3-celular \n 4-email \n 5-documento \n 6-obra social"))
        match(selector):
            case 1:
                nombre=input("ingrese nuevo nombre: ")
                instruccion=f"UPDATE pacientes SET nombre='{nombre}' WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 2:
                apellido=input("ingrese nuevo apellido: ")
                instruccion=f"UPDATE pacientes SET apellido='{apellido}' WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 3:
                celular=input("ingrese nuevo celular: ")
                instruccion=f"UPDATE pacientes SET celular='{celular}' WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 4: 
                email=input("ingrese nuevo email: ")
                instruccion=f"UPDATE pacientes SET email='{email}'WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 5:
                documento=input("ingrese nuevo documento: ")
                instruccion=f"UPDATE pacientes SET documento={documento} WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 6:
                obra_social=input("ingrese nuevo nro obra_social: ")
                instruccion=f"UPDATE pacientes SET documento={obra_social} WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 7:
                conn.close()
                pass
    else:
 
                instruccion=f"UPDATE pacientes SET nombre='{nombre}' WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
           
                instruccion=f"UPDATE pacientes SET apellido='{apellido}' WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                
                instruccion=f"UPDATE pacientes SET celular='{celular}' WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                
           
                instruccion=f"UPDATE pacientes SET email='{email}'WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                
         
                instruccion=f"UPDATE pacientes SET documento={documento} WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                
                instruccion=f"UPDATE pacientes SET documento={obra_social} WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                
                conn.close()
               

conexion()




if __name__ == "__main__":
    conexion()
    elegir=int(input("1-agregar paciente\n 2-eliminar paciente \n 3-modificar paciente"))
    match (elegir):
        case 1:
            nombre=input("seleccione nombre: ")
            apellido=input("seleccione apellido: ")
            celular=input("seleccione celular: ")
            email=input("seleccione email: ")
            documento=int(input("seleccione documento: "))
            obra_social=int(input("seleccione obra social: "))
            nuevo_paciente(nombre,apellido,celular,email,documento,obra_social)
        case 2:
            nombre=input("seleccione nombre: ")
            apellido=input("seleccione apellido: ")
            eliminar_paciente(nombre,apellido)
        case 3:
            documento=int(input("seleccione documento: "))
            modificar_paciente(documento)