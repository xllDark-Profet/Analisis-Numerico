import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

datos = pd.read_csv('datos prueba.csv', header =0)
print (datos)

def f(x, a, b):
    return a*np.exp(-b*x**2)

res, cov= curve_fit(fun, datos['x'], datos['y'])
print(res)

x = np.linspace(-5, 5 ,50)


fig, axes = plt.subplot()
axes.scatter(datos['x'], datos['y'])
axes.plot(x, fun()) #Aqui tienes que poner los valores de res
plt.show()