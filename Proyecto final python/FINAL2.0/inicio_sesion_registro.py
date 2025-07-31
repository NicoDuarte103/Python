import sqlite3 as sql
from ASIGNACION_TURNO import *
from PIL import Image, ImageTk


def conexion():
    conn=sql.connect("registro.db")
    cursor=conn.cursor()
    instruccion= """CREATE TABLE IF NOT EXISTS registro(
                                            usuario text,
                                            contraseña text,
                                            documento text)"""
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def crear_usuario(usuario,contraseña,documento):
    conn=sql.connect("registro.db")
    cursor=conn.cursor()
    instruccion=f"INSERT INTO registro VALUES('{usuario}','{contraseña}','{documento}')"
    
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
def eliminar_usuario(usuario):
    conn=sql.connect("registro.db")
    cursor=conn.cursor()
    instruccion=f"DELETE FROM registro WHERE usuario='{usuario}'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    print(f"usuario: {usuario} eliminado")
def cambiar_contraseña(documento,contraseña):
    
    conn=sql.connect("registro.db")
    cursor=conn.cursor()
    comprobacion=f"SELECT * from registro WHERE documento='{documento}'"
    cursor.execute(comprobacion)
    resultado_comprobacion=cursor.fetchall()
    conn.commit()
    conn.close()
    if resultado_comprobacion:
        
        #contraseña=input("ingrese nueva contraseña: ")
        conn=sql.connect("registro.db")
        cursor=conn.cursor()
        instruccion=f"UPDATE registro SET contraseña='{contraseña}' WHERE documento = '{documento}'"
        cursor.execute(instruccion)
        conn.commit()
        conn.close()

def inicio_sesion(usuario,contraseña):
    conn=sql.connect("registro.db")
    cursor=conn.cursor()
    instruccion=f"SELECT * from registro WHERE usuario ='{usuario}' and contraseña ='{contraseña}'"
    cursor.execute(instruccion)
    resultado= cursor.fetchall()
    conn.commit()
    conn.close()
    if resultado:
        #inicio sesion
        saludo()
    else:
        print("usuario y contraseña equivocados")

def menu():
    selector = int(input("bienvenido al sistema de registro que desea hacer?\n 1= registrarse\n 2= iniciar sesion \n 3= cambiar contraseña \n 4= eliminar usuario\n 5=salir\n" ))
    match(selector):
        case 1:
            usuario=input("ingrese su usuario: ")
            contraseña= input("ingrese su contraseña: ")
            documento= input("ingrese su numero de documento: ")
            celular=input("ingrese su celular: ")
            crear_usuario(usuario,contraseña,celular,documento)
        case 2:
            usuario=input("ingrese su usuario: ")
            contraseña= input("ingrese su contraseña")
            inicio_sesion(usuario,contraseña)

        case 3:
            documento=input("ingrese su dni: ")
            cambiar_contraseña(documento)
        case 4:
            usuario=input("ingrese su usuario: ")
            eliminar_usuario(usuario)
        case 5:
            print("ha salido del programa")
            pass

conexion()
    #mejoras
    #1- que los usuarios no puedan repetirse
    #2- claves alfanumericas y encriptacion con hashes
    #3- vincular ventanas
    #4-envio de codigo para cambio de clave
