import matplotlib.pyplot as plt

# # INGRESO , Datos de prueba
# xi = np.array([100, 200, 300, 400, 500 , 600])
# fi = np.array([-160, -35, -4.2, 9, 16.9, 21.3])

# # PROCEDIMIENTO
# # Polinomio de Lagrange
# n = len(xi)
# x = sym.Symbol('x')
# polinomio = 0
# divisorL = np.zeros(n, dtype = float)
# for i in range(0,n,1):

#     # Termino de Lagrange
#     numerador = 1
#     denominador = 1
#     for j  in range(0,n,1):
#         if (j!=i):
#             numerador = numerador*(x-xi[j])
#             denominador = denominador*(xi[i]-xi[j])
#     terminoLi = numerador/denominador

#     polinomio = polinomio + terminoLi*fi[i]
#     divisorL[i] = denominador

# # simplifica el polinomio
# polisimple = polinomio.expand()

# # para evaluación numérica
# px = sym.lambdify(x,polisimple)

# # Puntos para la gráfica
# muestras = 101
# a = np.min(xi)
# b = np.max(xi)
# pxi = np.linspace(a,b,muestras)
# pfi = px(pxi)

# # SALIDA
# print('Polinomio de Lagrange: ')
# print(polisimple)


import numpy as np
import sympy as sp


def intLagrange(x, y, u=None):
    n = len(x)
    if u == None:
        t = sp.Symbol('t')

    else:
        t = u
    p = 0
    for i in range(0, n):
        l = 1
        for j in range(0, n):
            if j != i:
                l = l * (t - x[j]) / (x[i] - x[j])
        p = p + y[i] * l
        p = sp.expand(p)
    return p


x = [0.0,0.04,0.08, 0.1, 0.11, 0.12, 0.13, 0.16, 0.20, 0.23, 0.25]
y = [10,18, 7, -8, 110, -25, 9, 8, 25, 9, 9]
p = intLagrange(x, y)

print(p)  # Polinomio de interpolacion
a = intLagrange(x, y, 450)  # Evaluar el polinomio en otro punto
print(a)

# #Gráfica
plt.plot(x, y, 'o', label='Puntos')
plt.legend()
plt.xlabel('x')
plt.ylabel('Y')
plt.title('Interpolación Lagrange')
plt.show()