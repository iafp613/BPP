from tkinter import *
from math import *


# Funciones

def boton(num):
    '''
    Función que se encarga de escribir en la pantalla
    '''
    global operacion
    operacion = operacion + str(num)
    texto_intro.set(operacion)

def resultado():
    '''
    Función que se encarga de calcular el resultado
    '''
    global operacion
    try:
        operacion = str(eval(operacion))
        texto_intro.set(operacion)
    except:
        texto_intro.set("ERROR")
        operacion = ""

def limpiar():
    '''
    Función que se encarga de limpiar la pantalla
    '''
    global operacion
    operacion = ""
    texto_intro.set("")


# Inicio de la aplicación y configuración de la misma

ventana = Tk()
ventana.title("Calculadora científica")
ventana.geometry("408x600")
ventana.resizable(0,0)
ventana.config(bg="burlywood4")

ancho_boton = 10
alto_boton = 2
color_boton = 'peachpuff3'
texto_intro = StringVar()
operacion = ''
salida = Entry(ventana, font=('consolas', 20, 'bold'), width=23, textvariable=texto_intro, bd=20, insertwidth=4, bg='skyblue1', justify='right').place(x=10, y=60)


# Botones de la calculadora: configuración y formato
boton0 = Button(ventana, text="0", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton(0)).place(x=17, y=180)
boton1 = Button(ventana, text="1", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton(1)).place(x=107, y=180)
boton2 = Button(ventana, text="2", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton(2)).place(x=197, y=180)
boton3 = Button(ventana, text="3", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton(3)).place(x=287, y=180)
boton4 = Button(ventana, text="4", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton(4)).place(x=17, y=240)
boton5 = Button(ventana, text="5", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton(5)).place(x=107, y=240)
boton6 = Button(ventana, text="6", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton(6)).place(x=197, y=240)
boton7 = Button(ventana, text="7", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton(7)).place(x=287, y=240)
boton8 = Button(ventana, text="8", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton(8)).place(x=17, y=300)
boton9 = Button(ventana, text="9", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton(9)).place(x=107, y=300)
botonPi = Button(ventana, text="π", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton('pi')).place(x=197, y=300)
botonComa = Button(ventana, text=",", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton('.')).place(x=287, y=300)
botonSuma = Button(ventana, text="+", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton('+')).place(x=17, y=360)
botonResta = Button(ventana, text="-", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton('-')).place(x=107, y=360)
botonMult = Button(ventana, text="*", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton('*')).place(x=197, y=360)
botonDivision = Button(ventana, text="/", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton('/')).place(x=287, y=360)
botonRaiz = Button(ventana, text="√", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton('sqrt(')).place(x=17, y=420)
botonParA = Button(ventana, text="(", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton('(')).place(x=107, y=420)
botonParB = Button(ventana, text=")", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton(')')).place(x=197, y=420)
botonPorcentaje = Button(ventana, text="%", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton('%')).place(x=287, y=420)
botonln = Button(ventana, text="ln", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton('log(')).place(x=17, y=480)
botonLimpiar = Button(ventana, text="C", bg=color_boton, width=ancho_boton, height=alto_boton, command=limpiar).place(x=107, y=480)
botonExp = Button(ventana, text="EXP", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:boton('**')).place(x=197, y=480)
botonIgual = Button(ventana, text="=", bg=color_boton, width=ancho_boton, height=alto_boton, command=resultado).place(x=287, y=480)





ventana.mainloop()