from scipy import optimize
import numpy as np
from array import array
import matplotlib.pyplot as plt


def f(x):
    return ((3*(x**4))-(61*(x**2))-(57*x)+310)

x = np.linspace(start=-10, stop=10, num=100)
plt.plot(x, f(x))
plt.grid()
plt.axhline(y=0, linewidth=2, c='k')
plt.axvline(x=0, linewidth=2, c='k')
#plt.show()

respuesta = optimize.fixed_point(f, x0=[2,4.5], xtol=2**-16)
print(respuesta)
