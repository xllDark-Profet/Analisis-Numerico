import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
def intLagrange(x,y,u=None):
  n=len(x)
  if u==None:
    t=sp.Symbol('t')

  else:
    t=u
  p=0
  for i in range(0,n):
    l=1
    for j in range (0,n):
      if j!=i:
        l=l*(t-x[j])/(x[i]-x[j])
    p=p+y[i]*l
    p=sp.expand(p)
  return p

x=[100, 200, 300, 400, 500 , 600]
y=[-160, -35, -4.2, 9, 16.9, 21.3]
p=intLagrange(x,y)




print (p) #Polinomio de interpolacion
a=intLagrange(x,y,450) #Evaluar el polinomio en otro punto
print(a)

# #Gráfica
plt.plot(x,y,'o', label = 'Puntos')
plt.legend()
plt.xlabel('x')
plt.ylabel('Y')
plt.title('Interpolación Lagrange')
plt.show()