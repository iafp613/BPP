'''
##################################################
Asignatura: Programación avanzada con Python
Alumno: Ignacio Alberto Fontal Patac
Fecha: 27/10/2021
Tema 4: Clases y objetos
##################################################
Enunciado:
Crea una clase calculadora que pueda ser utilizada de la siguiente manera:
calculadora = calculadora(num1, num2)
calculadora.sumar()
calculadora.multiplicar()
calculadora.restar()
calculadora.dividir()
-------------------------------------------------
'''

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def sumar(self):
        suma = self.num1 + self.num2
        print("Suma: ", suma)

    def restar(self):
        resta = self.num1 - self.num2
        print("Resta: ", resta)

    def multiplicar(self):
        multiplicacion = self.num1 * self.num2
        print("Multiplicación: ", multiplicacion)

    def dividir(self):
        try:
            division = self.num1 / self.num2
            print("División: ", division)

        except:
            print("División: No se puede dividir entre cero")

calculadora = Calculadora(5, 0)
calculadora.sumar()
calculadora.multiplicar()
calculadora.restar()
calculadora.dividir()