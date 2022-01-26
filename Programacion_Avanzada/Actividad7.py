'''
##################################################
Asignatura: Programación avanzada con Python
Alumno: Ignacio Alberto Fontal Patac
Fecha: 15/11/2021
Tema 9: Paralelismo y concurrencia
##################################################
Enunciado:
Crea un script el cual mediante la librería ‘threading’ o ‘_thread’ permita ejecutar 
una funcion simple (por ejemplo una función con un print) con diferentes hebras.
-------------------------------------------------
'''

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        print("Inicio " + self.name)
        print_time(self.name, 2)
        print('Hola, soy la hebra: {}'.format(self.name))
        print("Fin " + self.name)
    def __del__(self):
        print("Destruyendo hebra: " + self.name)

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

MyThread("Hilo 1").start()
MyThread("Hilo 2").start()
MyThread("Hilo 3").start()
MyThread("Hilo 4").start()
