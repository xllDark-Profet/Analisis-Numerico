# Algoritmo de punto fijo
# [a,b] intervalo de búsqueda
# error = tolera

import numpy as np
import math


def puntofijo(gx, a, tolera, iteramax=100):
    i = 1  # iteración
    b = gx(a)
    tramo = abs(b-a)
    while(tramo >= tolera and i <= iteramax):
        a = b
        b = gx(a)
        tramo = abs(b-a)
        i = i + 1
        print("iteracion:" , i)
        print("raiz:" , b)

    respuesta = b
 
# INGRESO

#def gx(x): return np.exp(-x)
def gx(x):return ((3*(x**4))-(61*(x**2))-(57*x)+310)

a = 2     # intervalo
b = 4,5
tolera = 2**-16

# PROCEDIMIENTO
puntofijo(gx, a, tolera)



