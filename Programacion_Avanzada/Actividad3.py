'''
##################################################
Asignatura: Programación avanzada con Python
Alumno: Ignacio Alberto Fontal Patac
Fecha: 19/10/2021
Tema 3: Programación y manejo de funciones
##################################################
Enunciado:
Escribe una función que acepte dos variables numéricas y calcule la suma y
la resta de dichas cifras. La función devolverá tanto la suma como la resta.
Utiliza las excepciones para controlar algún posible error dentro de la
función.
-------------------------------------------------
'''

print("###### EJERCICIO 1 #######")

def sumaResta(x, y):
    '''Esta función calcula la suma y la resta de dos números pasados por parámetros.
    Parámetros:
    -------------------------
    x ---> int, float
    y ---> int, float

    return:
    -------------------------
    tuple ---> Resultado de la suma y de la resta.
    '''
    try:
        suma = x + y
        resta = x - y

        print(f"El resultado de sumar y restar {x} y {y} es, respectivamente:")
        return suma, resta
    except:
        return "El valor introducido no es correcto"

print(sumaResta(68, 72))


'''
#################################################
Crea una función en la cual el segundo parámetro sea un argumento
predeterminado.
#################################################
'''

print("\n\n###### EJERCICIO 2 #######")

def sumaResta613(x, y=613):
    '''Esta función calcula la suma y la resta de un número con el número 613.
    Parámetros:
    -------------------------
    x ---> int, float
    y ---> 613

    return:
    -------------------------
    tuple ---> Resultado de la suma y de la resta con 613.
    '''
    try:
        suma = x + y
        resta = x - y

        print(f"El resultado de sumar y restar {x} y {y} es, respectivamente:")
        return suma, resta
    except:
        return "El valor introducido no es correcto"

print(sumaResta613(57))