'''
Filename: /home/javier/ejercicios3/ejercicio 3.1.py
Path: /home/javier/ejercicios3
Created Date: Wednesday, October 14th 2020, 10:32:26 am
Author: Javier Ortega

Copyright (c) 2020 Your Company
'''

import math
#import asegura_entrada
from asegura_entrada import *
from datetime import *

# Crear una función que calcule las raíces de un polinomio de segundo grado del tipo: ax^2 + bx +c
# discriminante = math.sqrt(b ** 2 - 4 * a * c)
# x1 = (-b + discriminante) / (2 * a)
# x2 = (-b - discriminante) / (2 * a)
# Para probar:
# a=1 b=1 y c=1 -> None
# a=1 b=2 y c=1 -> (-1, -1)
# a=2 b=3 y c=1 -> (-0.5, -1)
# a=0 b=3 y c=1 -> None

def calcula_raices_2grado(a, b, c):
    try:
        discriminante = math.sqrt(b ** 2 - 4 * a * c)
    except ValueError:
        return None
    try:
        x1 = (-b + discriminante) / (2 * a)
        x2 = (-b - discriminante) / (2 * a)
    except ZeroDivisionError:
        return None
    return (x1, x2)

# main
if __name__=="__main__":
    print("""
    Bienvenido/a al programa para calcular las raices de la ecuación de segundo grado
    ax² + bx + c
    """)

    hora_inicio = datetime.now()

    a = asegura_numero("a: ", funcion_tipo = tipo_float)
    b = asegura_numero("b: ", funcion_tipo = lambda t : float(t))
    c = asegura_float("c: ")

    resultado = calcula_raices_2grado(a, b, c)
    print(resultado)

    hora_fin = datetime.now()
    print(hora_fin-hora_inicio)
