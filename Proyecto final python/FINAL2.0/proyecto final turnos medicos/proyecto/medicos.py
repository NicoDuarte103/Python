import sqlite3 as sql

def conexion():
    conn=sql.connect("medicos.db")
    cursor=conn.cursor()
    instruccion= """CREATE TABLE IF NOT EXISTS medicos(
                                            nombre text,
                                            apellido text,
                                            celular text,
                                            email text,
                                            documento integer,
                                            especialidad text,
                                            matricula integer)"""
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def nuevo_medico(nombre,apellido,celular,email,documento,especialidad,matricula):
    conn=sql.connect("medicos.db")
    cursor=conn.cursor()
    instruccion=f"INSERT INTO medicos VALUES('{nombre}','{apellido}','{celular}','{email}',{documento},'{especialidad}',{matricula})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def eliminar_medico(nombre,apellido):
    conn=sql.connect("medicos.db")
    cursor=conn.cursor()
    instruccion=f"DELETE FROM medicos WHERE nombre='{nombre}' and apellido='{apellido}'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    print(f"nombre: {nombre},{apellido} eliminado")

def modificar_medico(nombre,apellido,celular,email,documento,especialidad,matricula):
    conn=sql.connect("medicos.db")
    cursor=conn.cursor()
    if __name__ == "__main__":
        selector=int(input("que desea modificar \n 1-nombre \n 2-apellido \n 3-celular \n 4-email \n 5-documento\n 6-especialidad\n 7-matricula"))
        match(selector):
            case 1:
                nombre=input("ingrese nuevo nombre: ")
                instruccion=f"UPDATE medicos SET nombre='{nombre}' WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 2:
                apellido=input("ingrese nuevo apellido: ")
                instruccion=f"UPDATE medicos SET apellido='{apellido}' WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 3:
                celular=input("ingrese nuevo celular: ")
                instruccion=f"UPDATE medicos SET celular='{celular}' WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 4: 
                email=input("ingrese nuevo email: ")
                instruccion=f"UPDATE medicos SET email='{email}'WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 5:
                documento=input("ingrese nuevo documento: ")
                instruccion=f"UPDATE medicos SET documento={documento} WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 6:
                especialidad=input("ingrese nuevo especialidad: ")
                instruccion=f"UPDATE medicos SET especialidad='{especialidad}' WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 7:
                matricula=input("ingrese nuevo matricula: ")
                instruccion=f"UPDATE medicos SET matricula='{matricula}' WHERE documento = {documento}"
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
            case 8:
                conn.close()
                pass
    else:
        instruccion=f"UPDATE medicos SET nombre='{nombre}' WHERE documento = {documento}"
        cursor.execute(instruccion)
        conn.commit()
        
    
        instruccion=f"UPDATE medicos SET apellido='{apellido}' WHERE documento = {documento}"
        cursor.execute(instruccion)
        conn.commit()
        
    
        instruccion=f"UPDATE medicos SET celular='{celular}' WHERE documento = {documento}"
        cursor.execute(instruccion)
        conn.commit()
        
    
        instruccion=f"UPDATE medicos SET email='{email}'WHERE documento = {documento}"
        cursor.execute(instruccion)
        conn.commit()
        
    
        instruccion=f"UPDATE medicos SET documento={documento} WHERE documento = {documento}"
        cursor.execute(instruccion)
        conn.commit()
       
    
        instruccion=f"UPDATE medicos SET especialidad='{especialidad}' WHERE documento = {documento}"
        cursor.execute(instruccion)
        conn.commit()
      
    
        instruccion=f"UPDATE medicos SET matricula='{matricula}' WHERE documento = {documento}"
        cursor.execute(instruccion)
        conn.commit()
        
        conn.close()
conexion()
if __name__=="__main__":
    conexion()
    elegir=int(input("1-agregar medico\n 2-eliminar medico \n 3-modificar medico"))
    match (elegir):
        case 1:
            nombre=input("seleccione nombre: ")
            apellido=input("seleccione apellido: ")
            celular=input("seleccione celular: ")
            email=input("seleccione email: ")
            documento=int(input("seleccione documento: "))
            especialidad=input("seleccione especialidad: ")
            matricula=int(input("seleccione matricula: "))
            nuevo_medico(nombre,apellido,celular,email,documento,especialidad,matricula)
        case 2:
            nombre=input("seleccione nombre: ")
            apellido=input("seleccione apellido: ")
            eliminar_medico(nombre,apellido)
        case 3:
            documento=int(input("seleccione documento: "))
            nombre=input("seleccione nombre: ")
            apellido=input("seleccione apellido: ")
            celular=input("seleccione celular: ")
            email=input("seleccione email: ")
            documento=int(input("seleccione documento: "))
            especialidad=input("seleccione especialidad: ")
            matricula=int(input("seleccione matricula: "))
            modificar_medico(nombre,apellido,celular,email,documento,especialidad,matricula)