
#Realizado por :
#Andres Ricardo Porras Escobar
#Cristian Camilo Benitez Peña
#Juan Alejandro Diaz Lote

from math import*


def aitken(x,datos): 
  
 
  arr=(datos[1]-datos[0])**2
  abb=datos[2]-(2*datos[1])+datos[0]
  div= arr/abb

  x=datos[0]-div
 

  datos[0]= datos[1]
  datos[1]= datos[2]
  datos[2]= x
  return x

#punto 1 
#def g(x): return (cos(x))

#punto 2
def g(x): return (1/sin(x))

#punto 3
#def g(x): return ((1/27)*(3*x-2)**3)

#punto 5 
#def g(x): return (5/(-2 + x**2))

datos = [0,0,0]
t1= 10**-8;
t2= 10**-16;
t3= 10**-32;
t4= 10**-56;
print("a:", t1)
print("b:", t2)
print("c:", t3)
print("d:", t4)
te =input("Escoja una tolerancia: ")

if te == "a":
  te= t1 

if te == "b":
  te= t2

if te == "c":
  te= t3 
     
if te == "d":
  te= t4 
  

x=1
x=g(x)
datos[0]=x
print("valor inicial: ", x)

era=1
cont= 0

while( era > te ):
 x1=x
 x=g(x1)
 
 if cont==2 :
   datos[1]= x1
  
 if cont==3 :
  datos[2]= x1
  

 while(cont>=3 and era > te):
   x=aitken(x,datos)
  
  
   era= abs(x-x1)
   cont=cont+1

   print(" iteracion ", cont)
   print(x)

 era= abs(x-x1)
 cont= cont +1
 print(" iteracion ", cont)
 print(x)



