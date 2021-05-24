from numpy import*
def vandermonde (x):
  n=len(x)
  d=zeros([n,n])
  for i in range (n):
   for j in range (n):
     d[i][j]=x[i]**(n-j-1)
  dt=1
  for i in range (n):
    for j in range (n):
      if j<i:
        dt=dt*(x[j]-x[i])
  c=linalg.cond(d, inf)
  return [d,dt,c]

x=[100, 200, 300, 400, 500 , 600]
y=[-160, -35, -4.2, 9, 16.9, 21.3 ]
[d,dt,c]=vandermonde(x)
print (d) #Matriz de vandermonde
print(dt) #Determinante de la matriz
print (c) #Numero de condicion
a=linalg.solve(d,y) #Solucion
print(a)