'''
ASIGNATURA: Programación de Aplicaciones con Python
ALUMNO: Ignacio A. Fontal Patac
FECHA: 08/01/2022
ACTIVIDAD: Tema 14 - PyWebIO
'''

from pywebio.input import *
from pywebio.output import *

comanda = input_group(
    'Pedido', 
    [
        input('Nombre:', name='Nombre', type=TEXT),
        input('Mesa:', name='Mesa', type=NUMBER),
        input('Edad:', name='Edad', type=NUMBER),
        checkbox('¿Qué desea beber?', options=['Coca-cola', 'Agua', 'Cerveza', 'Vino de la casa'], name='Bebida'),
        checkbox('¿Qué desea comer?', options=['Pizza', 'Hamburguesa', 'Ensalada', 'Pescado'], name='Comida'),
        select('¿Va a pagar con tarjeta?', options=['Si', 'No'], name='Tarjeta')
    ])

put_text = 'Resumen pedido'

put_table([
    ['Nombre', comanda['Nombre']], 
    ['Mesa', comanda['Mesa']],
    ['Edad', comanda['Edad']],
    ['Bebida', comanda['Bebida']],
    ['Comida', comanda['Comida']],
    ['Tarjeta', comanda['Tarjeta']]
])

popup('¡Muchas gracias por su pedido!', '¡Su pedido ha sido registrado!')