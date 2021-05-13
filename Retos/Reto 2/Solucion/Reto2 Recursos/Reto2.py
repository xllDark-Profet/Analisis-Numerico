#REALIZADO POR:
#ANDRES RICARDO PORRAS ESCOBAR
#CRISTIAN CAMILO BENITEZ
#JUAN ALEJANDRO DIAZ LOTE

#IMPORTACIONES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
from scipy.interpolate import InterpolatedUnivariateSpline


#DECLARACIONES
xls=pd.ExcelFile('pruebasTemperatura.xlsx')
datos=xls.parse('DataS1')

#INTERPOLACION
x= np.linspace(min(datos['DataN']), max(datos['DataN']), num=10001)
yld= np.interp(x,datos['DataN'],datos['TemperaturaSelect'])
ysp= InterpolatedUnivariateSpline(datos['DataN'],datos['TemperaturaSelect'])(x)


plt.plot(datos['DataN'],datos['TemperaturaSelect'],'o',mew=2)
plt.plot(x,yld)
plt.plot(x,ysp)
leg = plt.legend(['Datos','Lineal',' Spline Cubico'])
leg.get_frame().set_facecolor('#fafafa')
plt.show()
