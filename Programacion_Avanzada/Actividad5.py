'''
##################################################
Asignatura: Programación avanzada con Python
Alumno: Ignacio Alberto Fontal Patac
Fecha: 30/10/2021
Tema 5: Trabajando con colecciones
##################################################
Listas:
Utiliza una lista para almacenar los números del 1 al 10 la cual debe ser rellenada
con el uso de un bucle while. Finalmente muestra la lista en orden inverso
-------------------------------------------------
'''
contador = 1
lista = []

while contador < 11:
    lista.append(contador)
    contador += 1

print(lista)
print(lista[::-1])

'''
Diccionarios:
1. Crea un diccionario con 4 valores.
2. Muestra los valores del diccionario.
3. Modifica el 3º valor del diccionario
4. Añade un nuevo valor al diccionario de tipo lista
5. Muestra nuevamente los valores
-------------------------------------------------
'''
# 1
my_dict = {
    'peso': 25,
    'altura': 60,
    'nombre': 'Labrador',
    'color': 'canela'
}

# 2
print(my_dict.values())

# 3
my_dict['nombre'] = 'Golden'

# 4
my_dict['genetica'] = ['1BH3', 'ACTG', '9J-H13B']

# 5
print(my_dict.values())