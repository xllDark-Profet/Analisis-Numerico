import numpy as np
from scipy.optimize import root_scalar
import math
import matplotlib.pyplot as plt


def f(x):
    return ((x**3) - (2*(x**2)) + ((4*x)/3) - (8/27))


# graficar parqa recocnocer el intervalo 
x = np.linspace(start=-10, stop=10, num=100)
plt.plot(x, f(x))
plt.grid()
plt.axhline(y=0, linewidth=2, c='k')
plt.axvline(x=0, linewidth=2, c='k')
#plt.show()

solucion = root_scalar(f, method='brentq', bracket=[0, 2], rtol=(2**-80))
print(f"Metodo de Brent:\n\
     - raiz= {solucion.root}\n\
     - Iteraciones ={solucion.iterations}\n")
