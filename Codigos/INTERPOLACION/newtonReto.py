import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO , Datos para la prueba
xi = np.array([32.09,36.64,36.98,36.55,38.35,31.83,35.81,38.49,31.6,28.07,26.54,25.91,25.39,25.05,24.33,27.56,25.93,24.72,23.95,23.21,23.05,23.08,32.03,32.66,32.66,35.04,35.67,37.41,37.69,39.44,34.39,30.93,28.36,26.6,25.98,25.35,24.68,29.04,33.56,34.88,35.97,36.77,38.64,39.81,40.64,38.52,35.27,29,26.25,24.68,23.64,23.03,22.99,34.2,35.45,36.9,38.66,39.54,41.88,40.87,36.56,31.94,28.41,26.18,24.96,24.26,23.88,23.6,26.94,28.93,30.46,32.01,32.5,36.59,40.57,40.69,40.72,34.36,29.74,26.98,25.91,25.69,25.56,25.6,25.51,33.58,35,36.48,38.2,38.95,39.79,39.4,38.17,34.17,28.93,27.14,26.29,25.32,24.67,25.04])
fi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100])

# PROCEDIMIENTO

# Tabla de Diferencias Divididas Avanzadas
titulo = ['i   ', 'xi  ', 'fi  ']
n = len(xi)
ki = np.arange(0, n, 1)
tabla = np.concatenate(([ki], [xi], [fi]), axis=0)
tabla = np.transpose(tabla)

# diferencias divididas vacia
dfinita = np.zeros(shape=(n, n), dtype=float)
tabla = np.concatenate((tabla, dfinita), axis=1)

# Calcula tabla, inicia en columna 3
#tamaño de la matriz
[n, m] = np.shape(tabla)
diagonal = n - 1
j = 3
while (j < m):
    # cada fila de columna
    i = 0
    paso = j - 2  # inicia en 1
    while (i < diagonal):
        denominador = (xi[i + paso] - xi[i])
        numerador = tabla[i + 1, j - 1] - tabla[i, j - 1]
        tabla[i, j] = numerador / denominador
        i = i + 1
    diagonal = diagonal - 1
    j = j + 1

# POLINOMIO con diferencias Divididas
# caso: puntos equidistantes en eje x
dDividida = tabla[0, 3:]
n = len(dfinita)

# expresión del polinomio con Sympy
x = sym.Symbol('x')
polinomio = fi[0]
for j in range(1, n, 1):
    factor = dDividida[j - 1]
    termino = 1
    for k in range(0, j, 1):
        termino = termino * (x - xi[k])
    polinomio = polinomio + termino * factor

# simplifica multiplicando entre (x-xi)
polisimple = polinomio.expand()

# polinomio para evaluacion numérica
px = sym.lambdify(x, polisimple)

# Puntos para la gráfica
muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a, b, muestras)
pfi = px(pxi)

# SALIDA
print('polinomio con Newton: ')
print(polisimple)
c = 1
while (c < 100):
  solucion = px(c)
  print(solucion)
  c = c+1


# Gráfica
plt.plot(xi, fi, 'o', label='Puntos')
plt.plot(pxi, pfi, label='Polinomio')
plt.legend()
plt.xlabel('Indices')
plt.ylabel('Temperatura')
plt.title('Diferencias Divididas - Newton')
plt.show()