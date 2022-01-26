'''
##################################################
Asignatura: Programación avanzada con Python
Alumno: Ignacio Alberto Fontal Patac
Fecha: 08/11/2021
Tema 7: Trabajando con BBDD
##################################################
Enunciado:
Crea en Python una función que genere una BBDD Sqlite3 
Partiendo  de  la  BBDD  generada,  crea  una  función  que  genere  las  siguientes 
tablas: 
• Una tabla con 4 campos 
• Una tabla con 2 campos
-------------------------------------------------
'''

import sqlite3


def create_conexion():
    try:
        conexion = sqlite3.connect("FONTAL_PATAC_BD_Act7_ProAva.sqlite")
        print("Conexion establecida")
        print(conexion)
        return conexion
    except sqlite3.Error as error:
        print("Error al conectar con la base de datos")
        print(error)
        return None

def create_table(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT NOT NULL,
                            apellido TEXT NOT NULL,
                            edad INTEGER NOT NULL,
                            email TEXT NOT NULL
                            )""")
        print("Tabla 1 creada")
        cursor.execute("""CREATE TABLE IF NOT EXISTS trabajo(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            posicion TEXT NOT NULL,
                            empresa TEXT NOT NULL
                            )""")
        print("Tabla 2 creada")
    except sqlite3.Error as error:
        print("Error al crear la tabla")
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print("Conexion cerrada")

'''
Crea una función para cada una de las siguientes sentencias que opere sobre las 
tablas creadas: 
• Insertar 
• Actualizar 
• Listar 
• Borrar
'''

def insertar(conexion, tabla, datos):
    try:
        if tabla == 'usuarios':
            cursor = conexion.cursor()
            cursor.execute("""INSERT INTO usuarios(nombre, apellido, edad, email)
                            VALUES(?,?,?,?)""", datos)
            conexion.commit()
            print("Datos insertados")
        elif tabla == 'trabajo':
            cursor = conexion.cursor()
            cursor.execute("""INSERT INTO trabajo(posicion, empresa)
                            VALUES(?,?)""", datos)
            conexion.commit()
            print("Datos insertados")
    except sqlite3.Error as error:
        print("Error al insertar datos")
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print("Conexion cerrada")

def actualizar(conexion, tabla, datos):
    try:
        if tabla == 'usuarios':
            cursor = conexion.cursor()
            cursor.execute("""UPDATE usuarios SET nombre = ?, apellido = ?, edad = ?, email = ?
                            WHERE id = ?""", datos)
            conexion.commit()
            print("Datos actualizados")
        elif tabla == 'trabajo':
            cursor = conexion.cursor()
            cursor.execute("""UPDATE trabajo SET posicion = ?, empresa = ?
                            WHERE id = ?""", datos)
            conexion.commit()
            print("Datos actualizados")
    except sqlite3.Error as error:
        print("Error al actualizar datos")
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print("Conexion cerrada")

def listar(conexion, tabla):
    try:
        if tabla == 'usuarios':
            cursor = conexion.cursor()
            cursor.execute("""SELECT * FROM usuarios""")
            resultado = cursor.fetchall()
            print("Datos de la tabla usuarios")
            for datos in resultado:
                print(datos)
        elif tabla == 'trabajo':
            cursor = conexion.cursor()
            cursor.execute("""SELECT * FROM trabajo""")
            resultado = cursor.fetchall()
            print("Datos de la tabla trabajo")
            for datos in resultado:
                print(datos)
    except sqlite3.Error as error:
        print("Error al listar datos")
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print("Conexion cerrada")

def borrar(conexion, tabla, datos):
    try:
        if tabla == 'usuarios':
            cursor = conexion.cursor()
            cursor.execute("""DELETE FROM usuarios WHERE id = ?""", datos)
            conexion.commit()
            print("Datos borrados")
        elif tabla == 'trabajo':
            cursor = conexion.cursor()
            cursor.execute("""DELETE FROM trabajo WHERE id = ?""", datos)
            conexion.commit()
            print("Datos borrados")
    except sqlite3.Error as error:
        print("Error al borrar datos")
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print("Conexion cerrada")

create_table(create_conexion())
insertar(create_conexion(), "usuarios", ("Ignacio", "Patac", 25, "iafp613@gmail.com"))
insertar(create_conexion(), "trabajo", ("Desarrollador", "Google"))
actualizar(create_conexion(), "usuarios", ("Ana", "Patac", 60, "user@user.com", 2))
actualizar(create_conexion(), "trabajo", ("Data Scientist", "Microsoft", 2))

print("\n####### TABLA USUARIOS ######")
listar(create_conexion(), "usuarios")

print("\n####### TABLA TRABAJO ######")
listar(create_conexion(), "trabajo")

borrar(create_conexion(), "usuarios", (2,))
borrar(create_conexion(), "trabajo", (2,))

