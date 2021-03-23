 
from numpy import*
import numpy as np

# Hecho por
#  Juan Alejandro Diaz Lote
# Andres Ricardo Porras
# Crian Camilo Benitez

#punto 4 con gaussSeidel

def gaussseidel(a,b,x):
    n=len(x)
    for i in range(n):
        s=0
        for j in range(n):
            if i!=j:
                s=s+a[i][j]*x[j]
        x[i]=(b[i]-s)/a[i][i]
    return x





def gaussseidelm(a,b,x,e,m):
    n=len(x)
    t=x.copy()
    for k in range(m):
        x=gaussseidel(a,b,x)
        print("Iteracion",k)
        print("el valor de X es: ",x)
        d=np.linalg.norm(array(x)-array(t),inf)
        if d<e:
            
            return [x,k]
        else:
            t=x.copy()
    return [[],m]





#como la matriz debe ser extrictamente diagonal dominante se escogieron valores
#para alpha entre 0 y 1 y para delta valores mayores a 2

a=[[2,0,-1],[0.1,2,-1],[-1,1,3]]
b=[1.5,2,1.6666]
x=[1,2,3]
iteMax= 20
tol = 10**-54
print("METODO  GAUSS SEIDEL")
x=gaussseidelm(a,x,b,tol,iteMax)
