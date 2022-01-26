'''
##################################################
Asignatura: Programación avanzada con Python
Alumno: Ignacio Alberto Fontal Patac
Fecha: 18/10/2021
##################################################
Enunciado:
Escribe un programa que pida un número por pantalla. A continuación, mediante
un bucle se mostrarán por pantalla todos los números enteros desde el 0 hasta
el número introducido por pantalla.
-------------------------------------------------
'''
# Primero debemos comprobar que el usuario ha introducido un número correcto
# Un número válido sería cualquier número entero o flotante, positivo o negativo, incluyendo el cero
# Un número no válido sería cualquier caracter alfabético o el cero negativo

import re # Importamos regex
import numpy as np

print("###### EJERCICIO 1 #######")

num = input("Escribe un número: ")

num_format = re.compile(r'^(?!-0?(\.0+)?$)-?(0|[1-9]\d*)?(\.\d+)?(?<=\d)$') # Esta expresión recoge los elementos del string
it_is = re.match(num_format, num) # Esta expresión devuelve True si cumple la condición o False si no

# Entra en el bucle si es un número válido.
if it_is:
    entero = re.compile(r'[+-]?(?<!\.)\b[0-9]+\b(?!\.[0-9])') # Recoge si el input contiene el punto flotante o no
    es_entero = re.match(entero, num)

    # Entra si no contiene un punto flotante, por tanto es entero
    if es_entero:
        num = int(num) # Convierte el string en número entero

        # Entra si es un entero positivo
        if num > 0:
            for i in range (0, num + 1):
                print(i)

        # Entra si es un entero negativo
        elif num < 0:
            for i in range(num, 0 + 1):
                print(i)

        # Entra si el número = 0
        else:
            print(0)

    # Entra si contiene un punto flotante, por tanto es flotante
    else:
        flotante_pos = re.compile(r'^(0|[1-9]\d*)(\.\d+)?$') # Recoge si el input flotante es positivo o no.
        es_flotante_pos = re.match(flotante_pos, num)
        num = float(num)
        decimal = num - int(num)

        # Entra si es un número flotante positivo
        if es_flotante_pos:
            for i in range(0, int(num) + 1):
                print(i + decimal)

        # Entra si es un número flotante negativo
        else:
            for i in range(int(num), 0 + 1):
                print(i + decimal)

# Si no es un número válido
else: print("No has introducido un número válido")


'''
#################################################
Crea un diccionario con unos valores cualquiera y muestra únicamente mediante
un bucle for los valores de este.
#################################################
'''
print("\n\n###### EJERCICIO 2 #######")

import json # Importamos la librería JSON simplemente para ver más bonito el diccionario por pantalla.

diccionario = {
    "Nombre": "Nacho",
    "Edad": 35,
    "Hermanos": True,
    "Altura": 182,
    "Perros": ["Lisa", "Lola", "Lupita"],
    "Edades perros": {
        "Lisa": 10,
        "Lola": 5,
        "Lupita": 12
    },
    "Peso": "76 Kg"
}

print("\n--- Mi diccionario: ---\n", json.dumps(diccionario, sort_keys=False, indent=4))

# Si tan solo queremos obtener las claves del diccionario:
print("\n---Las claves del diccionario son:---\n", diccionario.keys())

# Si tan solo queremos obtener los valores del diccionario:
print("\n---Los valores del diccionario son:--- \n", diccionario.values())

# Pero si queremos darle un formato de clave - valor que sea bonito:
print("\n\n--- MI DICCIONARIO ---\n")
for clave, valor in diccionario.items():
    print("El valor de la clave %s es %s" % (clave, valor))
