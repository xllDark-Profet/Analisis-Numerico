
#Realizado por :
#Andres Ricardo Porras Escobar
#Cristian Camilo Benitez Peña
#Juan Alejandro Diaz Lote

from math import *
from numpy import *

t1 = 10**-8
t2 = 10**-16
t3 = 10**-32
t4 = 10**-56
print("a:", t1)
print("b:", t2)
print("c:", t3)
print("d:", t4)
te = input("Escoja una tolerancia: ")

if te == "a":
    te = t1

if te == "b":
    te = t2

if te == "c":
    te = t3

if te == "d":
    te = t4

#punto 1 =0.7390851332151607
def g(x): return (cos(x))

#punto 2= 1.1141571440916247
#def g(x): return (1/sin(x))

#punto 3= No se aproxima diverge
#def g(x): return ((1/27)*(3*x-2)**3)

#punto 5 = Entra en un ciclo infinito
#def g(x): return (5/(-2 + x**2))

x = 1
x = g(x)
print("valor inicial: ", x)

era = 1
cont = 0
datos=[]

while (era >= te):

    x1 = x
    x = g(x)
    era = abs(x - x1)
    
    if cont >500:
      exit(0)

    cont = cont + 1
    print(" iteracion ", cont)
    print(x)
   
